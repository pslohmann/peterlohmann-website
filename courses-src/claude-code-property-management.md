---
title: "Claude Code for Property Managers: APIs, Alerts, and Automation"
slug: "claude-code-property-management"
date: 2026-10-30
description: "Connect your property management software to Claude Code, forecast lease endings, catch negative owner balances in Slack, and run it all on a schedule."
youtube_id: "2IyTPI2neRw"
upload_date: 2026-10-11
duration: "PT20M33S"
thumbnail: ""
tags: ["Technology", "Operations"]
sponsor_domains: ["rentvine.com"]
---

A lot of property managers are sleeping on Claude. I ask Claude Code which months have the most leases ending, and a couple of minutes later I have a chart to share with my team so they can plan for upcoming turns. I also have checks running that catch owner balances that don't match between the software we use.

I've been using it in my business for a few months, and it's helped me run more profitably, cut down on problems and inefficiencies, and get information to everyone who needs it. The final system I built prepares our month-end owner distribution worksheet and saves me about eight hours of manual work every month.

This course takes you through three levels: connecting one piece of software to Claude Code, connecting the tools you need to run checks across your business, and getting all of it running on a schedule. It's for PM owners and operators who've never written a line of code. You don't need to.

## What you'll learn

- Get an API key from your property management software and plug it into Claude Code
- Ask plain-English questions about your business and forecast lease endings for turn planning
- Build a weekly Slack alert that flags negative owner balances by property manager
- Reconcile properties and units across your software so you stop paying for inactive doors
- Move your automations to a virtual private server and schedule them with cron jobs

## Get your first API key {t=01:18}

> [!TAKEAWAY]
> Claude Code goes from a useful chatbot to a business workhorse once you give it API access to software you already use. Start with one key.

Claude Code isn't just for programmers. Don't let the word "code" put you off. It's the most powerful version of Claude, and you can use it to do amazing things as the owner or operator of a property management company.

1. **Download the Claude desktop app** and make sure it's updated to the latest version.
2. **Open Claude Code.**
3. **Pick one piece of software you use every day.** Ideally your main property accounting software. For me that's Buildium. For you it might be AppFolio, Rentvine, Propertyware, RealPage, or something else.
4. **Check whether your plan includes API access.** A lot of these platforms charge extra for an API key. My software does, and it's not cheap; I had to upgrade earlier this year to get API access. The notable exception is Rentvine, which makes API keys available regardless of plan.
5. **If your main software won't give you a key, use a different tool.** You likely use tools like Property Meld or RentEngine, and if you dig in, you'll find a lot of them offer API keys.

Not sure whether your software offers API access? Ask Claude Code. Tell it you run a property management business, list the software you use, and ask how to get API keys for a few of them. It'll likely research the API documentation on the web, tell you whether your plan includes access, and give you step-by-step instructions to get the key.

The goal for this step is one API key, from one tool you use every day.

## Plug the key in and ask questions {t=03:50}

> [!TAKEAWAY]
> Tell Claude Code what you want, give it your key and the API documentation, start with read-only access, and ask plain-English questions about your business.

1. **Tell Claude Code what you're trying to do.** Something like: "I'm a property management business owner. We use Rentvine, and I want to plug my Rentvine API key into you so I can ask questions about my business: occupancy, leasing, maintenance tickets, whatever it is."
2. **Use a strong model.** I use Opus 5.5 or higher for this. Fable works too, but it's more expensive. Opus 5.5 works great and is relatively inexpensive in terms of usage.
3. **Follow its instructions to add the key.** It'll walk you through getting the key and either have you paste it into the chat or give you a more secure way to provide it.
4. **Point it to the API documentation.** Every API works a little differently, they change over time, and Claude Code doesn't know every API ever built. Giving it the docs for your software helps it communicate correctly.
5. **Ask for read-only access to start.** That keeps you safe and prevents accidentally overwriting important data.

Once the key is in, you can ask plain-English questions about your business. If you connected maintenance coordination software, try:

- How many open work orders do we have?
- What's the average tenant rating on our maintenance requests?
- How many vendors are active in the system?
- Do you see any duplicate units?

> [!WARNING]
> **Skipping read-only mode.** Until you know what you're doing, tell Claude Code to stick to read-only access so it can't overwrite data your business depends on.

## Forecast lease endings and build dashboards {t=05:37}

> [!TAKEAWAY]
> With your accounting software connected, you can ask for forecasts and build custom dashboards that pull from multiple sources, which used to take a developer or a BI tool.

Once your property accounting software is connected, some of my favorite questions are:

- What's our average rent?
- How many units are active in the system right now?
- "I'm trying to forecast my turns for the next year. Can you give me a graph showing upcoming lease endings (or move-outs) broken down by month?"

For that last one, Claude Code reads your rent roll and gives you back a graph that helps you forecast workload, staffing, and capacity for the next season or two of turns.

### Dashboards that weren't possible before

Most of the tools we use have built-in dashboards, and they're great as far as they go. But as soon as I see a dashboard, I have ideas for other data to add, or how much more powerful it would be with data from multiple sources.

Business intelligence (BI) dashboards have been around for decades, but small business owners couldn't really use them. You needed an expensive developer to write custom software, or you had to figure out something like Microsoft Power BI. That's no longer the case. With a few API keys plugged into Claude Code, you can ask it to build a real-time owner's dashboard that pulls from multiple sources. You can even connect your email and Slack.

> [!NOTE]
> A lot of these platforms have AI built in, with a chat window that answers questions about your data. That's useful, but you're stuck on their platform: no custom reporting, and no combining data from different sources into one picture of your business.

## Catch negative owner balances in Slack {t=08:01}

> [!TAKEAWAY]
> Have Claude Code pull rental owner balances, find owners who are negative across all their properties, and post them to Slack by property manager every week.

> [!STAT] $50,000 | Negative owner balances caught in the first couple of months

### Connect Slack

If you haven't already, connect Slack to Claude Code. Just ask: "I'd like to connect Slack. How can I do that?" It may ask whether you need two-way communication or just notifications. Notifications are usually enough here, and they keep the setup simpler.

### The problem

If you manage third party, you have a trust account, and every owner you work for has a balance inside it. In a perfect world, those balances never go negative. (Of course, that would never happen at your company. It certainly never happened at mine.) Just in case, you want to know right away.

For owners with multiple properties, you look at the sum across all their properties:

| Property | Balance |
|---|---|
| Property A | -$500 |
| Property B | +$700 |
| **Owner total** | **$200** |

An owner total of $200 is not a trust account violation. If the total across all their properties is negative (or a single-property owner is negative), that's an issue, and your team needs to know immediately.

![Owner balance math: Property A at -$500 plus Property B at +$700 equals an owner total of $200, which is not a trust account violation](/courses/assets/claude-code-property-management/claude-code-property-management-owner-balance.svg)
*Sum every property before you call it a violation.*

Our software didn't notify us when an owner went negative. We'd find it when we ran disbursements once a month. The longer a negative balance sits, the harder it is to fix: the owner forgets, the property manager doesn't remember the details, the account may sink further, and the problem gets worse.

### The fix

Before Claude Code, I didn't know how to solve this. I could have hired a programmer for a long, expensive build, and if it broke I'd have no idea how to fix it. With Claude Code, I built and deployed it in an afternoon. When it has broken, I pull up the same chat session and get it working again.

1. **Have Claude Code pull rental owner ending balances** from your accounting software.
2. **Filter out inactive properties.**
3. **Sum each owner's balances across all their properties.**
4. **Keep only owners who are negative overall.**
5. **Check its answer against your own report.** I can run a similar report directly in my software. When Claude Code got it wrong, I'd sometimes just paste a screenshot of the correct report and ask what the problem was. It figured it out, fixed it, and got it right from then on.
6. **Group the results by property manager.** In my company, every owner is assigned to one of three or four property managers, and that person is the one who'll actually fix the balance.
7. **Post it to Slack.** List each owner, their negative balance, and which properties it's on, grouped by property manager, and tag any property manager with owners on the list.
8. **Schedule it.** Ours runs once a week (more on scheduling below).

None of this was coding. I was typing into Claude Code what I wanted. Now the report posts to our Slack channel every week, tags the right property manager, and they fix the problem before it gets out of hand. We don't wait until month-end anymore, and I sleep better knowing it's catching these before they turn into big legal issues.

## Reconcile properties and units across your software {t=12:54}

> [!TAKEAWAY]
> Connect every system you pay for by the unit, and have Claude Code audit which properties are active where. You'll find doors you're still paying for after you demanaged them.

> [!STAT] 690 vs. 730 | Active properties in our accounting software vs. Property Meld

I have Claude Code connected to our accounting software and to Property Meld, our maintenance coordination software. When you run multiple systems and you're constantly onboarding and offboarding properties, they drift out of sync. In a given month, we're probably onboarding 10 to 20 new properties and offboarding 10 to 15.

When I'd check manually, about once a year, I'd find things like 690 active properties in our accounting software and 730 in Property Meld. That doesn't make sense, and it costs money: most of these platforms charge by the unit, so you're paying every month for properties that may not need to be active.

So I had Claude Code build a checker that talks to every system through its API, inventories the properties, units, and owners, and flags discrepancies. Every time I run it, I find a few properties that are active in one system and inactive in another, often ones we demanaged 6 months ago.

To set up your own, tell Claude Code something like:

> "I'm trying to make sure I don't have any properties or units active in these softwares that don't need to be, because they sometimes go out of sync when we demanage a property. Please connect to these APIs and inventory and audit this. Run it once a week (or once a month) and send me an email or tag me in Slack with the results."

It saves money and saves your team headaches by automating checks that were too manual to bother with.

> [!NOTE]
> This video is sponsored by Rentvine. Rentvine has offered a free, open API with no limits from day one, and its new MCP (Model Context Protocol) connects Claude, ChatGPT, and other AI tools to your live Rentvine data under your own permissions, at no extra cost.

## Move your automations to a server {t=16:07}

> [!TAKEAWAY]
> Automations that live on your laptop stop when your laptop does. Rent a cheap virtual private server and have Claude Code move everything over through GitHub.

Once you have checks and reports running, you may wonder: do I have to leave my computer on all the time? What happens if I take my laptop to a conference, the power goes out, or my computer crashes? As set up so far, everything stops.

The fix is a **VPS (virtual private server)**: a computer in the cloud that you lease. Everything you've built with Claude Code moves there and runs in a data center instead of on your laptop.

You don't need to know much about servers, because Claude Code will walk you through it:

1. **Sign up for a VPS.** I use Hetzner and chose one of their cheaper plans.
2. **Tell Claude Code what you want.** I said: "I just signed up for a VPS with Hetzner. I want to move everything we've done together (the API access, the Slack updates, the owner balance checks) over to the VPS, but I don't know anything about servers. Please walk me through this step by step."
3. **Follow its steps.** It'll have you log in to your VPS provider and set up a secure connection (an SSH key, for example), then install what it needs on the server.
4. **Set up GitHub.** Claude Code will likely use GitHub, a tool programmers use to keep track of their code. Sign up for an account and connect it to Claude Code on your computer. When you work on something locally, Claude Code pushes it to GitHub, and from there it deploys to your VPS, so the server always runs the latest version.
5. **When you get stuck, paste a screenshot.** I constantly screenshot an error and paste it into Claude Code: "Here's what I'm seeing. What do I do now?" Learn your screenshot shortcut, or bind one to a key, because you'll use it a lot.

![Deployment flow: Claude Code on your computer pushes to GitHub, GitHub deploys to your VPS, scheduled cron jobs run there, and results go to Slack or email](/courses/assets/claude-code-property-management/claude-code-property-management-deploy-flow.svg)
*Build on your computer, run on the server.*

## Schedule it with cron jobs {t=19:14}

> [!TAKEAWAY]
> Once your VPS and GitHub are connected, tell Claude Code to deploy everything and run each job on a schedule, with results sent to Slack or email.

Tell Claude Code: "Now that you're connected to my VPS and GitHub, deploy everything we worked on to the VPS, and I want it to run on this schedule."

Claude Code sets up **cron jobs** on your VPS, which are just scheduled tasks. A job can run every five minutes, every 15 minutes, once a day, every Monday at a set time, on the 10th of every month, or whatever you need. Each job sends its output wherever you want: a Slack notification, an email, or any other tool it's connected to.

## The month-end owner distribution worksheet {t=20:04}

> [!TAKEAWAY]
> My worksheet tool tells the team exactly how much to distribute to each owner, so we don't send back money an owner just paid us for a turn or repair.

> [!STAT] 8 hrs | Manual work the worksheet saves me every month

The tool I built with Claude Code prepares a worksheet that tells us exactly how much money to distribute to each owner at month-end. It prevents a mistake I've made by accident before: sending money back to an owner who just sent us money for something like a turn or a maintenance request.

I wrote a full newsletter article on how the worksheet works: [read it here](https://peter.beehiiv.com/p/peter-lohmann-s-newsletter-tuesday-edition-33).

## Resources mentioned

- **[Owner distribution worksheet (newsletter article)](https://peter.beehiiv.com/p/peter-lohmann-s-newsletter-tuesday-edition-33):** how the month-end worksheet works.
- **[Rentvine MCP](https://www.rentvine.com/features/mcp):** connects Claude, ChatGPT, and other AI tools to your live Rentvine data (this video's sponsor).
- **Claude desktop app and Claude Code:** where all of this runs.
- **Hetzner:** the VPS provider I use.
- **GitHub:** keeps track of your code and deploys it to your server.
