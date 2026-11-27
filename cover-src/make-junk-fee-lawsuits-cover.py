"""Nov 27, 2026 cover: "Junk-Fee Lawsuits Against PM Software: Where 7 Cases Stand" (DARK).
A rent checkout card (navy, light rim) whose "Convenience fee +$0.67" row is the orange highlight,
and a gavel that has just come down on its sound block beside it. Minimal words, icon-heavy.
Writes cover-src/<slug>.html; render at 1200x675 (see CLAUDE.md), then images/blog/<slug>--cover.webp."""
import os
from cover_kit import page, DARK, NAVY, NAVY2, EDGE, BLUE, ORANGE, BAR, icon
SLUG = "junk-fee-lawsuits-property-management-software"
F = 'font-family="Inter, Helvetica Neue, Arial, sans-serif"'

card = f"""
<ellipse cx="380" cy="350" rx="330" ry="260" fill="url(#glowB)"/>
<g filter="url(#rim)">
  <rect x="150" y="105" width="460" height="470" rx="30" fill="{NAVY}" stroke="{EDGE}" stroke-width="2"/>
</g>
<g filter="url(#lift)"><rect x="150" y="105" width="460" height="470" rx="30" fill="{NAVY}" stroke="{EDGE}" stroke-width="2"/></g>
<rect x="150" y="105" width="460" height="92" rx="30" fill="{NAVY2}"/><rect x="150" y="167" width="460" height="30" fill="{NAVY2}"/>
{icon("house", 204, 151, 34, "#fff", 2.2)}
<text x="236" y="163" {F} font-weight="800" font-size="33" fill="#fff">Pay rent</text>
<rect x="196" y="236" width="150" height="16" rx="8" fill="{BAR}" opacity=".55"/>
<rect x="436" y="236" width="128" height="16" rx="8" fill="{BAR}" opacity=".55"/>
<rect x="196" y="282" width="110" height="16" rx="8" fill="{BAR}" opacity=".35"/>
<rect x="460" y="282" width="104" height="16" rx="8" fill="{BAR}" opacity=".35"/>
<ellipse cx="380" cy="368" rx="230" ry="70" fill="url(#glowO)"/>
<rect x="178" y="330" width="404" height="78" rx="18" fill="{ORANGE}"/>
<text x="204" y="378" {F} font-weight="700" font-size="25" fill="#fff">Convenience fee</text>
<text x="556" y="381" {F} font-weight="800" font-size="34" fill="#fff" text-anchor="end">+$0.67</text>
<line x1="196" y1="446" x2="564" y2="446" stroke="{EDGE}" stroke-width="2" stroke-dasharray="2 9"/>
<rect x="196" y="478" width="368" height="62" rx="31" fill="{BLUE}"/>
{icon("check", 352, 509, 28, "#fff", 2.6)}
<text x="374" y="519" {F} font-weight="800" font-size="27" fill="#fff">Pay</text>
"""

# Gavel: head stands upright on the sound block, handle runs up and to the right.
gavel = f"""
<ellipse cx="905" cy="505" rx="250" ry="170" fill="url(#glowO)" opacity=".55"/>
<g filter="url(#lift)">
  <ellipse cx="880" cy="548" rx="150" ry="34" fill="{NAVY2}" stroke="{EDGE}" stroke-width="2"/>
  <path d="M730 520v28a150 34 0 0 0 300 0v-28" fill="{NAVY2}" stroke="{EDGE}" stroke-width="2"/>
  <ellipse cx="880" cy="520" rx="150" ry="34" fill="{NAVY}" stroke="#7FB4DD" stroke-opacity=".55" stroke-width="2"/>
</g>
<g filter="url(#rim)" transform="rotate(-14 880 420)">
  <rect x="930" y="396" width="270" height="27" rx="13.5" fill="#c9d8e4" transform="rotate(-30 930 409.5)"/>
  <rect x="1128" y="390" width="70" height="39" rx="19.5" fill="{ORANGE}" transform="rotate(-30 930 409.5)"/>
  <rect x="818" y="318" width="124" height="190" rx="22" fill="#e8eef3"/>
  <rect x="806" y="318" width="148" height="34" rx="12" fill="{ORANGE}"/>
  <rect x="806" y="474" width="148" height="34" rx="12" fill="{ORANGE}"/>
  <rect x="818" y="396" width="124" height="26" fill="#c9d8e4"/>
</g>
<g stroke="#f3a57f" stroke-width="5" opacity=".9">
  <path d="M700 470l-34-14"/><path d="M694 508h-40"/><path d="M700 546l-34 14"/>
  <path d="M1062 470l34-14"/><path d="M1068 508h40"/><path d="M1062 546l34 14"/>
</g>
"""
if __name__ == "__main__":
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), f"{SLUG}.html")
    css = '\n  @import url("https://fonts.googleapis.com/css2?family=Inter:wght@700;800&display=block");'
    open(out, "w", encoding="utf-8").write(page(DARK, card + gavel, css))
    print("wrote", SLUG)
