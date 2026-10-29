# Claude Code for Property Managers: APIs, Alerts, and Automation

- Author: Peter Lohmann (property management operator; owner of RL Property Management, Columbus, Ohio)
- Published: 2026-10-30
- Video: https://www.youtube.com/watch?v=2IyTPI2neRw
- Course page: https://peterlohmann.com/courses/claude-code-property-management/
- Topics: Claude Code, AI for property management, property management software APIs, lease-ending forecasts, business intelligence dashboards, trust account negative owner balances, Slack alerts, software reconciliation, virtual private server (VPS), GitHub, cron jobs, owner distribution worksheet
- Sponsor disclosure: the video is sponsored by Rentvine.

## Summary

I use Claude Code at my property management company to forecast lease endings, catch negative owner balances, reconcile properties across software, and prepare our month-end owner distribution worksheet, which saves me about eight hours of manual work each month. None of it required programming; I described what I wanted in plain English. The method has three levels: connect one piece of software to Claude Code with an API key; connect several tools and Slack to run checks across the business; then move everything to a virtual private server and run it on a schedule. This course is for property management owners and operators with no coding background.

## Key terms

- **Claude Code:** the most powerful version of Anthropic's Claude, available in the Claude desktop app. It is not only for programmers.
- **API key:** a credential from a software platform that lets Claude Code read (and optionally change) that platform's data.
- **API documentation:** the platform's published instructions for how its API works. Each API is different and APIs change, so Claude Code works best when pointed to the docs.
- **Read-only access:** permission to read data but not change it. I recommend starting with read-only access.
- **Rental owner ending balance:** an owner's balance inside the property management company's trust account.
- **Negative owner balance:** an owner whose balance, summed across all of their properties, is below zero. This is a trust account problem that should be fixed quickly.
- **VPS (virtual private server):** a computer in the cloud that you lease, so automations keep running when your own computer is off.
- **GitHub:** a tool programmers use to keep track of code. Claude Code uses it to deploy code from your computer to the VPS.
- **Cron job:** a scheduled task on a server, such as a report that runs every Monday or on the 10th of every month.
- **MCP (Model Context Protocol):** a standard that connects AI tools to software data. Rentvine offers an MCP that connects Claude, ChatGPT, and other AI tools to live Rentvine data under the user's own permissions.

## Prerequisites

- The Claude desktop app, updated to the latest version, with access to Claude Code.
- At least one software platform that provides an API key, ideally the main property accounting software.
- A Slack workspace for alerts (optional but recommended).
- For scheduling: a VPS account (I use Hetzner) and a GitHub account.

## Step-by-step

1. Install and update the Claude desktop app, then open Claude Code.
2. Get one API key.
   1. Choose a platform you use every day, ideally your main property accounting software. I use Buildium. Others include AppFolio, Rentvine, Propertyware, and RealPage.
   2. Check whether your plan includes API access. Many platforms charge extra. My software charges quite a bit, and I upgraded earlier this year to get API access. Rentvine makes API keys available regardless of plan.
   3. If your main platform will not give you a key, get one from another tool you use, such as Property Meld or RentEngine.
   4. If you are unsure whether a platform offers API access, tell Claude Code you run a property management business, list your software, and ask how to get API keys. It will research the API documentation and give step-by-step instructions.
3. Connect the key to Claude Code.
   1. Tell Claude Code you are a property management business owner, name the software, and say you want to plug in your API key so you can ask questions about occupancy, leasing, maintenance tickets, and so on.
   2. Use Opus 5.5 or higher. Fable also works but costs more. Opus 5.5 works well and is relatively inexpensive in usage.
   3. Follow its instructions to provide the key, either by pasting it into the chat or by a more secure method it suggests.
   4. Point Claude Code to the platform's API documentation.
   5. Tell Claude Code to use read-only access for now, to avoid overwriting important data.
4. Ask plain-English questions. Examples for maintenance coordination software: How many open work orders do we have? What is the average tenant rating on our maintenance requests? How many vendors are active? Are there duplicate units? Examples for accounting software: What is our average rent? How many units are active right now?
5. Forecast lease endings. Ask Claude Code for a graph of upcoming lease endings or move-outs by month for the next year. It reads the rent roll and returns a chart that helps forecast workload, staffing, and capacity for upcoming turns.
6. Build custom dashboards. With several API keys connected, ask Claude Code to build a real-time owner's dashboard that combines data from multiple sources, including email and Slack. Built-in AI chat inside individual platforms cannot do custom reporting or combine data from multiple sources.
7. Connect Slack. Ask Claude Code how to connect Slack. Notification-only access is usually enough and simpler than two-way communication.
8. Build a negative owner balance alert.
   1. Have Claude Code pull rental owner ending balances from the accounting software.
   2. Filter out inactive properties.
   3. Sum each owner's balances across all of their properties. Example: an owner with one property at -$500 and another at +$700 has a total of $200, which is not a trust account violation.
   4. Keep only owners whose total is negative (including single-property owners with a negative balance).
   5. Verify the output against a similar report run directly in the accounting software. If Claude Code is wrong, paste a screenshot of the correct report and ask what the problem is.
   6. Group results by property manager. At my company, each owner is assigned to one of three or four property managers, who is the owner's primary contact and the person who will fix the balance.
   7. Post the report to Slack, listing each owner, their negative balance, and the affected properties, grouped by property manager, and tag each property manager who has owners on the list.
   8. Run it weekly. My report runs once a week. In its first couple of months, it caught over $50,000 in negative owner balances.
9. Reconcile properties and units across software.
   1. Connect every platform that charges by the unit, such as the accounting software and Property Meld.
   2. Ask Claude Code to inventory and audit properties, units, and owners across those APIs and flag properties that are active in one system and inactive in another.
   3. Schedule it weekly or monthly, with results sent by email or Slack.
   4. Context: my company onboards about 10 to 20 properties and offboards about 10 to 15 in a typical month. A manual check once showed 690 active properties in our accounting software and 730 in Property Meld. Each run of the checker finds a few properties still active in one system, sometimes 6 months after we demanaged them.
10. Move automations to a VPS.
    1. Sign up for a VPS. I use Hetzner on one of its cheaper plans.
    2. Tell Claude Code you signed up for a VPS, want to move everything you built (API access, Slack updates, owner balance checks) to it, know nothing about servers, and need step-by-step instructions.
    3. Follow its steps: log in to the VPS provider, set up a secure connection such as an SSH key, and let it install the needed software on the server.
    4. Create a GitHub account and connect it to Claude Code on your computer. Code you build locally goes to GitHub and then deploys to the VPS, so the server runs the latest version.
    5. When stuck, paste a screenshot of the error into Claude Code and ask what to do. Learn your computer's screenshot shortcut.
11. Schedule the jobs. Tell Claude Code to deploy everything to the VPS and run each job on a schedule. It sets up cron jobs that can run every five minutes, every 15 minutes, daily, weekly, on a set weekday, or on a set day of the month, and send results by Slack, email, or another connected tool.
12. Prepare the month-end owner distribution worksheet. My Claude Code tool produces a worksheet showing exactly how much to distribute to each owner, which prevents sending money back to an owner who just paid for something like a turn or a maintenance request. It saves me about eight hours of manual work each month. Details: https://peter.beehiiv.com/p/peter-lohmann-s-newsletter-tuesday-edition-33

## Decision rules

- If your main accounting software does not include API access on your plan, either upgrade or start with an API key from another tool you use.
- If you are not sure a platform offers API access, ask Claude Code to research it.
- If you are just starting, use read-only access.
- If you only need alerts, connect Slack for notifications only.
- If an owner's balances summed across all their properties are negative, flag it. If the total is positive, it is not a trust account violation, even if one property is negative.
- If Claude Code's report disagrees with your software's report, show it the correct report and ask it to find the problem.
- If your automations need to run when your computer is off, move them to a VPS.
- If a job needs to repeat, schedule it as a cron job.

## Common mistakes

- **Assuming Claude Code is only for programmers.** It is the most powerful version of Claude and needs no coding; you describe what you want in plain English.
- **Skipping API access.** Without API keys, Claude Code is a useful chatbot; with them it can work with your business data.
- **Not pointing Claude Code to the API documentation.** APIs differ and change. Give it the docs.
- **Starting with write access.** Fix: start read-only to avoid overwriting data.
- **Relying on built-in platform AI.** It is limited to one platform's data, with no custom reporting or cross-platform reports.
- **Finding negative owner balances only at month-end.** The longer a negative balance sits, the harder it is to fix. Fix: a weekly automated Slack alert.
- **Checking per property instead of per owner.** Fix: sum each owner's balances across all properties before flagging.
- **Letting software platforms drift out of sync.** You pay per unit for properties that should be inactive. Fix: a scheduled reconciliation across APIs.
- **Running automations only on a laptop.** They stop when the computer is off, traveling, or crashed. Fix: move them to a VPS.
- **Sending money back to an owner who just paid you.** Fix: a month-end owner distribution worksheet that calculates exactly what to distribute.

## Questions and answers

**Can property managers use Claude Code without knowing how to code?**
Yes. I don't program. I describe what I want in plain English, and when something is wrong I paste a screenshot and ask Claude Code to fix it.

**How do I connect my property management software to Claude Code?**
Get an API key from the software (ideally your main accounting software), tell Claude Code what you want to do, provide the key the way it suggests, point it to the API documentation, and start with read-only access.

**Which property management software includes API access?**
It varies by plan, and many platforms charge extra. Rentvine makes API keys available regardless of plan. My accounting software charges extra, so I upgraded. You can ask Claude Code to research whether your plan includes API access.

**How can I forecast lease endings and turns?**
With your accounting software connected, ask Claude Code for a graph of upcoming lease endings or move-outs by month for the next year. It reads the rent roll and returns a chart for workload, staffing, and capacity planning.

**How do I catch negative owner balances in my trust account?**
I have Claude Code pull rental owner ending balances, filter out inactive properties, sum each owner's balances across all properties, and post owners with a negative total to Slack, grouped by property manager, every week. It caught over $50,000 in negative balances in its first couple of months.

**Is one negative property a trust account violation if the owner has others?**
Look at the owner's total across all properties. An owner with one property at -$500 and another at +$700 has a total of $200, which is not a trust account violation. A negative total is a problem.

**How do I find properties that are active in one system but not another?**
Connect each system's API to Claude Code and ask it to inventory and audit properties, units, and owners and flag discrepancies. I found 690 active properties in our accounting software versus 730 in Property Meld, and each run still finds a few.

**Do I have to leave my computer on for Claude Code automations?**
Not if you move them to a VPS. I use Hetzner. Claude Code walks you through connecting to the server and deploying through GitHub.

**How do I schedule recurring reports with Claude Code?**
Once it is connected to your VPS and GitHub, tell Claude Code to deploy your work and run it on a schedule. It sets up cron jobs that can run anywhere from every few minutes to monthly and send results to Slack or email.

**What is an owner distribution worksheet?**
It is a month-end worksheet my Claude Code tool prepares that shows exactly how much to distribute to each owner, so we don't send back money an owner just paid for a turn or a repair. It saves me about eight hours a month.

## Video timestamps

- 00:00 Intro: how I use Claude Code in my business
- 01:18 Get your first API key
- 03:50 Plug the key in and ask questions
- 05:37 Forecast lease endings and build dashboards
- 08:01 Catch negative owner balances in Slack
- 12:54 Reconcile properties and units across your software
- 16:07 Move your automations to a server
- 19:14 Schedule it with cron jobs
- 20:04 The month-end owner distribution worksheet
