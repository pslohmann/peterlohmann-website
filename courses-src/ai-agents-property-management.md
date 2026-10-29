---
title: "How I Use AI Agents to Run My Business and My Life"
slug: "ai-agents-property-management"
date: 2026-10-30
description: "Set up Grok Bot with a chief of staff and specialized bots that recruit, hunt spam, track returns, maximize credit card points, and handle family medical admin."
youtube_id: "Mw2CKsZHs_o"
upload_date: 2026-10-18
duration: "PT39M03S"
thumbnail: ""
tags: ["AI", "Technology", "Productivity"]
---

Earlier this year I bought a Mac Mini to run OpenClaw, the open-source AI assistant everyone was talking about. It was cool for a while. Then the integrations kept breaking, and I spent more time restarting things and redoing connections than the assistant ever saved me. So I stopped using it.

I'm an engineer, so I care about inputs and outputs: does a tool return more time than it takes? Over the last 6 to 8 weeks, a wave of commercial AI agents has arrived, and the one I went all in on is Grok Bot. It's the first agent that's been a clear net gain for me, in my property management business and in my personal life.

This course walks through my actual setup: installing it, connecting accounts, and the specific bots that are doing real work for me. It's for owners who want an AI assistant that gets things done without hours of fiddling.

## What you'll learn

- Choose a maintained, commercial AI agent over an open-source one you have to babysit
- Set up Grok Bot on desktop and phone and understand how its virtual computer works
- Organize work into specialized bots, with a chief of staff bot that routes tasks to them
- Automate recruiting outreach, spam filtering, and purchase and return tracking
- Track credit card credits and points, and keep your family's medical admin in one place

## Why I switched to a commercial agent {t=01:23}

> [!TAKEAWAY]
> Open-source agents can eat more time than they save. Commercial agents cost money, but someone else maintains them, they improve constantly, and they're much easier to use.

Most of this year, after the initial OpenClaw excitement faded, not much happened in AI agents. In the last 6 to 8 weeks, there's been an explosion of capable new ones. The difference is that these are commercial products:

- **Downside:** they aren't free. They cost money.
- **Upside:** other people maintain them, they're constantly improving, and they're much easier to use.

I looked at a few and went all in on Grok Bot.

If you spend any time on X, you'll see a lot of hype and a lot of people doing what I was doing with OpenClaw: spending more time configuring the thing and exploring what's possible than using it to get time back. Everything in this course is something that has been a net gain for me, measured as time invested versus time the agent returned.

> [!WARNING]
> **Spending more time on the agent than it saves you.** If you're constantly fixing integrations or tinkering with settings, the agent isn't paying for itself.

## Set up Grok Bot and its virtual computer {t=03:13}

> [!TAKEAWAY]
> Install both the desktop and phone apps. Everything runs on a virtual computer in the cloud, so your bots, chats, and tools stay in sync everywhere.

Most of the new commercial agents give you two things: a phone app and a desktop app. Get both. They're useful in different situations.

These agents stay in perfect sync no matter where you use them. On my phone, desktop, or laptop, I see the same bots, the same history, and the same capabilities. One thing I still find frustrating with Claude is that my versions get out of sync, because some of the work happens on whichever computer I'm using.

Grok Bot avoids that because it runs a **virtual machine** for you in the cloud. You don't need to understand virtual machines. Think of it as a dedicated computer behind your bots where everything happens, instead of on your own computer. You can open it up and look at it: browsers, logins, files.

I tried to build something like this myself with a virtual private server (I used Hetzner back when I was running OpenClaw). It worked okay, but it was clunky. Logging into a server securely, let alone viewing its desktop, is not a trivial thing for a non-coder like me.

### Keep it updated

- **Update the app.** It's being updated about once a day right now. When an update is available, there's usually a box in the bottom left corner telling you.
- **Update or reset the computer once in a while.** In settings, Grok Bot's computer (its virtual machine) can be updated or reset, which restarts it. If you're missing a feature, this is often why. The traffic-routing setting below didn't show up for me until I updated the computer.

## Connect your accounts and create one bot per job {t=06:24}

> [!TAKEAWAY]
> Connect a core few accounts first, then create a separate bot for each category of work. Bots share the same virtual computer and logins, and they can hand tasks to each other.

1. **Download the desktop or phone app** and walk through setup.
2. **Connect your accounts early.** These agents get a hundred times more useful once your accounts are connected. During setup, it asks what you're using it for and which services you have. You can connect Gmail, Google Drive and Sheets, Slack, Dropbox, and most other services you use.
3. **Start with a core few.** Don't connect everything you've ever used. Learn what it can do, then add more over time.
4. **Create a separate bot for each category of work.** It works best when you split things into bots instead of one long conversation with one bot. Mine include a recruiter, buy/sell/returns, and Spam Hunter.
5. **Give each bot a description** of what you want it to do. You can also rename it, change its icon, and configure its voice, since you can talk to it.

The bots share one virtual computer, so if one bot has your Gmail login, they all do. They can hand tasks to each other and set up scheduled tasks.

I've also built and deleted several bots that weren't useful enough to keep. That's part of the process.

## Build a chief of staff and a morning brief {t=09:08}

> [!TAKEAWAY]
> A chief of staff bot takes general requests and routes them to the right specialist bot. Start it with a morning brief, then have it pick one to-do a day it can make progress on.

Everyone should set up a chief of staff bot. It acts as the architect for your fleet of bots. When I open the app on my phone, I don't have to find the right bot. I tell the chief of staff, it delegates to the right bot, and that bot does the work. Anything general goes to the chief of staff.

![Chief of staff routing: I send requests to the chief of staff, which routes them to five specialist bots: recruiter; buy, sell, returns; Spam Hunter; credit card points and travel; and medical admin](/courses/assets/ai-agents-property-management/ai-agents-property-management-chief-of-staff.svg)
*Tell the chief of staff. It finds the right bot.*

### The morning brief

A morning brief is the "hello world" of AI agents. Mine arrives at 7:00 a.m., and includes:

- **The date**
- **The weather,** including the dew point (those who know me know I care a lot about dew point)
- **My calendar,** formatted the way I want it. The first version was formatted badly, so I had it redo it until I liked it.
- **My Grok Bot usage**

I set it to arrive at 7:00 a.m. local time wherever I am. It knows where I am from my calendar, so if I'm in San Diego, I get it at 7:00 a.m. Pacific instead of Eastern.

For more ideas, just ask it: "What are some cool ideas I could add to my morning brief?" When I asked, it suggested calendar conflict callouts, a prep line for my first meeting, a kids-only line so their events don't get buried, my top three Todoist items, expiring credits and travel, and a one-line fun fact. Some were good, and some I didn't care about.

> [!NOTE]
> Usage is weekly, and in my opinion it's generous. I think I started with the $20 or $30 a month plan. There are sometimes free trials and specials when you sign up.

### Let it pick a task from your to-do list

My chief of staff reviews my Todoist inbox, where most of my tasks live, and once a day suggests one open task it thinks it can make progress on. Before it starts, it has to clear it with me, so it doesn't waste time.

One day it picked a lead magnet I'd had on my list forever: the software stack I'd recommend from 0 to 500 doors, offered as a way to get people to sign up for my newsletter. It offered to research it and bring me a reviewable draft. I replied directly to that message ("give it a shot"), so it had the context, and it got to work.

(I connected Todoist through its API. There may be a native connector, but it wasn't working for me.)

## Automate recruiting outreach {t=14:34}

> [!TAKEAWAY]
> My recruiter bot runs LinkedIn outreach for a local executive assistant through Dripify and reports back daily. It's net new work that otherwise wouldn't happen at all.

> [!STAT] 116 | People my recruiter bot has contacted, with 16 accepts and 12 replies

I have an executive assistant, Monica, in the Philippines, and she's awesome. But between multiple businesses and young kids at home, I need a local EA too: someone to run errands, help with videos, maybe pick up the kids or take the dog to the groomer. Prospecting for that role is time-consuming, and I didn't want to hire a recruiter for it.

### How I set it up

1. **Create a bot named Recruiter.** Because of the name, it already had an idea of what I wanted and offered options. I picked outreach and follow-ups, on LinkedIn.
2. **Give it the outreach plan.** It searched LinkedIn for people currently working as executive assistants in the Columbus metro area and sent connection requests with a note: I'm looking for an EA, here's a little about the job and the comp, let me know if you know anyone. I'd been doing this myself, and it was getting good responses.
3. **Throttle the volume.** I limited connection requests per day because I was worried LinkedIn would object.

### What went wrong, and the fix

It worked for about 24 hours. Then, even with throttling, LinkedIn flagged suspicious activity on my account and warned it might disable it. I paused and found two fixes:

- **Route traffic through your own computer.** In Grok Bot's settings, under computer, there's an option to route traffic through this computer. With it on, your agent's traffic looks like it's coming from your normal connection instead of a data center. Mine was off, which is why LinkedIn flagged it. More platforms, like Apple and Amazon, are starting to block AI agents, so this matters.
- **Use a dedicated outreach tool.** I asked my friend Dylan Scroggins, who does tons of recruiting (including for us at RL Property Management in the past), what he uses. He uses Dripify. I gave the bot a screenshot of the LinkedIn warning and told it to spin up a Dripify account and run all the candidate outreach there. It created the account (it handed control to me just for the password), paid for the trial through Link (a payment platform Grok Bot integrates with), carried over our outreach cadence, and started recruiting.

I've never logged into that Dripify account. I don't even know the right domain for the app.

### What it does now

It sends me a daily update. Dripify allows 20 invites a day, and on the day I recorded, it had sent 20 of 20, contacted 116 people, gotten 16 accepts and 12 replies. It tells me when I need to reply to someone, and it sends the job description to anyone who asks for it, all without input from me.

![Recruiting funnel: 116 people contacted, 16 accepted, and 12 replied](/courses/assets/ai-agents-property-management/ai-agents-property-management-recruiting-funnel.svg)
*Where the EA search stood on the day I recorded.*

If Grok Bot weren't doing this, it simply wouldn't happen. I know I need an EA, but it would fall to the bottom of my list every day. Now that I know about the traffic setting, I could probably run it natively through LinkedIn, but Dripify is working, so I'm letting it ride.

## Track purchases, sales, and returns {t=22:15}

> [!TAKEAWAY]
> Connect your email, and a buy/sell/returns bot can track orders, eBay listings, and returns. Share specific logins through 1Password when it needs to sign in somewhere.

Email is the gateway to everything: purchases, travel, projects, your whole history. Giving an agent access to it is the keys to the kingdom, and it's what makes these bots productive.

### On security

You may have concerns, and I get it. Everything in life is a trade-off. Every time you drive to the store, you take a risk. For me this trade-off is worth it, and I feel better doing it with commercial software: the company has something to lose if its bot goes rogue, and it's been tested by probably hundreds of thousands, if not millions, of users. That's very different from connecting your email to some open-source project where who knows what happens.

### What the bot does

- **Monitors things I'm selling,** like an old CPU I have listed on eBay
- **Keeps track of things I'm buying**
- **Helps with returns**

Not everything works the first time, and the hype people on social media don't always tell you that. When I asked when my new AirPods case would arrive (I left the old one at the Chicago airport), it couldn't get the answer. Apple hadn't sent a delivery date, so it tried to log into Apple and hit two-factor authentication.

### Taking over the virtual computer

When a bot hits a login it can't get past, it flags **action needed** and asks you to take over:

1. **Click take over.** You'll see Grok Bot's computer, with Chrome, a file manager, and a terminal.
2. **Log in yourself,** including the two-factor step.
3. **Click "I'm done, continue."** Don't start clicking around yourself. Now that you're logged in, the bot picks up from there.

### Sharing logins with 1Password

Grok Bot recently launched a 1Password integration. I'm a big 1Password user (it's how I share logins with my EA). It creates a shared vault, and you move specific logins into it, case by case, instead of handing over everything. I plan to share my Amazon, eBay, and other shopping logins so this bot can sign in and check on things.

## Hunt down spam automatically {t=27:20}

> [!TAKEAWAY]
> Spam Hunter checks my inbox three times a day, labels and archives spam, and learns from what I correct. If you get any real volume of spam, make this your first bot.

> [!STAT] 3x | Spam Hunter runs every weekday: 7:30 a.m., 11:00 a.m., and 3 p.m.

This is my favorite bot. If you've had an email address for a long time, you get a lot of spam: newsletters you didn't sign up for, marketing, podcast pitches, phishing attempts. Even with Gmail's filter and the one our IT provider puts on our domain, stuff gets through. Any LLM is smart enough to recognize spam when it sees it.

1. **Connect your email.** I connected my work email addresses.
2. **Tell it what counts as obvious spam.** For me, a lot of it is podcast pitches and vendors.
3. **Start cautious.** I asked it to dial up its aggressiveness slowly over time.
4. **Set the schedule.** Every weekday at 7:30 a.m., 11:00 a.m., and 3 p.m.
5. **Have it study your existing spam** so it learns what you already mark.
6. **Use a review label.** We created a Gmail label called Spam Hunter. On each run, it archives anything it thinks is spam and applies that label.
7. **Review the label every other day or so.** Look for legitimate email it caught by mistake. So far there hasn't been any. Then tell it to move what you've reviewed to spam.
8. **Let it learn from what it misses.** When I move something to spam myself, it knows that email came through and wasn't flagged, so it learns from the miss.

![Spam Hunter cycle: it runs three times a day, labels and archives spam, I review the label, and it learns from my corrections](/courses/assets/ai-agents-property-management/ai-agents-property-management-spam-hunter.svg)
*Each pass gets a little sharper.*

I don't want to think about how many hours and clicks I've spent on spam over the last 5 to 10 years. This is about to solve it for me.

## Maximize credit card points and travel perks {t=30:35}

> [!TAKEAWAY]
> Give a bot every card's benefits and point categories. It reminds you monthly about expiring credits, tells you which card to use where, and knows your travel perks.

This is my second favorite bot. If you have cards with points, category bonuses, or credits for things like Uber or hotels, it's hard to keep track of, and you end up leaving benefits on the table. Different cards earn different points in different categories (maybe 5x on gas with one card and 3x on travel with another), and once you add business cards, it's a mess.

I gave the bot all of my cards, my point balances with each, and screenshots of the bonus categories and rewards from the issuers' websites. Now it does three things:

1. **Monthly expiring-credit reminders.** My Chase Sapphire Reserve has credits (Chase Travel, dining, StubHub, Southwest, shops) that reset quarterly, every 6 months, or annually. The bot tracks what I have left and when it expires, and reminds me every month. I recently bought expensive soccer tickets and completely forgot about my StubHub credit. A monthly reminder would have caught that.
2. **Which card to use for what.** Based on rewards and relative point values, it told me which categories to put on each card. I don't really use my Amex, so I had it drop that card, and now it's simple: Sapphire Reserve for specific categories, and everything else on my X Money card, which is running 3% cash back right now.
3. **Travel perks on the spot.** In Chicago, I asked about lounge options flying domestic first class on United. It knows my cards, so it knew I have Priority Pass through the Sapphire Reserve. (There weren't great options that day, which wasn't the bot's fault.)

## Contacts, calendar, and family medical admin {t=35:09}

> [!TAKEAWAY]
> A contacts and calendar bot keeps both up to date, and a medical admin bot holds insurance details, tracks HSA receipts, and makes sure nobody in the family misses a checkup.

### Contacts and calendar

This one's simple. It's connected to my calendar and contacts and helps manage both. I can take a picture of a business card, and it adds the person to my contacts.

### Medical admin

Between health, dental, and vision insurance, multiple kids, an HSA, and a business, medical admin is a lot. We just switched health insurance companies at work, and I loaded everything into this bot.

- **Insurance cards:** I snap a photo of the front and back in the app, and it stores the details. It can help process claims.
- **HSA receipts:** it tracks HSA expenses so we can get reimbursed.
- **Appointments:** it has access to my calendar and our shared family calendar, keeps a record of everyone's dental, doctor, vision, and annual checkups, and makes sure we're keeping up, so nobody suddenly realizes it's been 3 years since their last dentist visit.
- **Applications:** health insurance applications ask when everyone in your family last visited any doctor. That used to mean digging through the calendar. Now I can ask the bot, or point it at the application and have it fill it out.

I'm barely scratching the surface of what's possible. The point is that this is the first AI agent that's been less work to set up than the value I get out of it.

> [!NOTE]
> I have no affiliate deal with Grok Bot and don't get any credits if you sign up. Similar agents worth a look: Muse from Meta, which has access to Instagram, Facebook, and Facebook Marketplace, and Instinct, which I think is invite-only right now.

## Resources mentioned

- **Grok Bot:** the AI agent this course is built on. Search for it and download the desktop and phone apps.
- **Dripify:** the LinkedIn outreach tool my recruiter bot runs.
- **Link:** the payment platform Grok Bot integrates with to approve payments.
- **1Password:** for sharing specific logins with Grok Bot through a shared vault.
- **Todoist:** where my tasks live; I connected it through its API.
- **Muse (Meta) and Instinct:** other AI agents with similar capabilities.
