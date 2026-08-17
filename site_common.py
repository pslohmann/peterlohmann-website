"""Shared head scripts + internal-link cleaning, used by every build script and the one-off
page patchers so all pages come out identical (clean extensionless links + the same head tags)."""
import re
from urllib.parse import urljoin

# --- head tracking scripts, injected right before </head> on every page ---
GA4 = ('<!-- Google Analytics (GA4) -->\n'
       '<script async src="https://www.googletagmanager.com/gtag/js?id=G-DRCVXMNK1D"></script>\n'
       '<script>window.dataLayer=window.dataLayer||[];function gtag(){dataLayer.push(arguments);}'
       "gtag('js',new Date());gtag('config','G-DRCVXMNK1D');</script>")

RB2B = ('<!-- RB2B -->\n'
        '<script>!function(key) {\n'
        'if (window.reb2b) return;\n'
        'window.reb2b = {loaded: true};\n'
        'var s = document.createElement("script");\n'
        's.async = true;\n'
        's.src = "https://b2bjsstore.s3.us-west-2.amazonaws.com/b/" + key + "/" + key + ".js.gz";\n'
        'document.getElementsByTagName("script")[0].parentNode.insertBefore(s, document.getElementsByTagName("script")[0]);\n'
        '}("0NW1GH7LKEO4");</script>')

def clean_links(html, page_path):
    """Rewrite internal *.html links to clean, root-relative, extensionless URLs that match the
    canonical tags + sitemap (e.g. index.html -> /, faq.html -> /faq, blog/x.html -> /blog/x).
    page_path is the current page's absolute path, e.g. "/faq.html" or "/blog/post.html"."""
    def repl(m):
        href = m.group(1)
        if re.match(r'(?:https?:)?//|^(?:mailto:|tel:|#)', href):
            return m.group(0)                      # external / anchor / protocol
        base = href.split('#')[0].split('?')[0]
        if not base.endswith('.html'):
            return m.group(0)                      # assets (.css/.svg/.png/...) and dir links: leave
        tail = href[len(base):]                    # keep #fragment / ?query
        ap = urljoin(page_path, base)              # resolve relative -> absolute /path
        if ap == '/index.html' or ap.endswith('/index.html'):
            ap = ap[:-len('index.html')]           # -> "/" or "/report/"
        elif ap.endswith('.html'):
            ap = ap[:-5]                            # drop .html
        return 'href="%s%s"' % (ap, tail)
    return re.sub(r'href="([^"]+)"', repl, html)

def finalize(html, page_path):
    """Inject head tracking (idempotent) then clean internal links. Used at every page write."""
    if 'G-DRCVXMNK1D' not in html:
        html = html.replace("</head>", GA4 + "\n</head>", 1)
    if 'window.reb2b' not in html:
        html = html.replace("</head>", RB2B + "\n</head>", 1)
    return clean_links(html, page_path)
