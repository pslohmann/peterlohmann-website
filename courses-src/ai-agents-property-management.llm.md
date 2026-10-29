# How I Use AI Agents to Run My Business and My Life

- Author: Peter Lohmann (property management operator; owner of RL Property Management, Columbus, Ohio)
- Published: 2026-10-30
- Video: https://www.youtube.com/watch?v=Mw2CKsZHs_o
- Course page: https://peterlohmann.com/courses/ai-agents-property-management/
- Topics: AI agents, AI personal assistant, Grok Bot, OpenClaw, chief of staff bot, morning brief, AI recruiting outreach, LinkedIn, Dripify, spam filtering, Gmail automation, purchase and return tracking, 1Password, credit card rewards, travel benefits, medical admin, HSA tracking
- Disclosure: since recording the video, I've joined Grok Bot's referral program. Grok Bot links on the course page are affiliate links, and I may get credit if you sign up: https://grok.com/refer/bot?code=MAQ7C63ZXZ83

## Summary

Earlier this year I ran OpenClaw, an open-source AI assistant, on a Mac Mini, but its integrations kept breaking and I spent more time maintaining it than it saved, so I stopped. In the last 6 to 8 weeks, commercial AI agents have arrived that cost money but are maintained, constantly improving, and much easier to use. I went all in on Grok Bot. It runs on a cloud virtual computer, stays in sync across phone and desktop, and lets me create specialized bots that share logins and hand tasks to each other. This course covers my setup and the bots that are a net time gain for me: a chief of staff with a morning brief, a recruiter, a buy/sell/returns tracker, Spam Hunter, a credit card points and travel bot, and contacts, calendar, and medical admin bots. It is for business owners who want an AI assistant that does real work without hours of configuration.

## Key terms

- **AI agent:** an AI personal assistant driven by a large language model with a harness that lets it use tools and accounts on your behalf.
- **Commercial agent:** a paid agent maintained by a company, as opposed to a free open-source agent you maintain yourself.
- **Grok Bot's computer (virtual machine):** a dedicated cloud computer where all of a user's bots do their work. Users can view it, open browsers, and log in to sites on it.
- **Bot:** a separate agent inside Grok Bot for one category of work. Bots share the same virtual computer and logins and can hand tasks to each other.
- **Chief of staff bot:** a bot that receives general requests and routes each one to the right specialist bot.
- **Morning brief:** a scheduled daily summary from an agent, such as the date, weather, and calendar.
- **Route traffic through this computer:** a Grok Bot setting that sends the agent's internet traffic through the user's own connection instead of a data center, so sites are less likely to flag it as suspicious.
- **Take over:** the step where a user controls Grok Bot's computer to complete a login (such as two-factor authentication), then hands control back.
- **Spam Hunter:** my spam-filtering bot, which labels and archives spam in Gmail on a schedule.

## Prerequisites

- A paid Grok Bot plan. I think I started on the $20 or $30 a month plan; usage is measured weekly.
- The Grok Bot desktop app and phone app.
- Accounts to connect, starting with email (Gmail) and calendar.
- Optional: 1Password for sharing specific logins, Todoist for tasks, a Dripify account for LinkedIn outreach.

## Step-by-step

1. Choose a commercial AI agent. Open-source agents like OpenClaw can cost more time in maintenance than they save. Commercial agents cost money but are maintained, improve constantly, and are easier to use. Judge any agent by whether it returns more time than it takes.
2. Install Grok Bot.
   1. Install both the desktop app and the phone app.
   2. Expect everything (bots, chat history, tools) to stay in sync across devices, because the work runs on Grok Bot's cloud virtual computer, not on your own computer.
   3. Keep the app updated. It currently updates about once a day; an update notice usually appears in the bottom left corner.
   4. Periodically update or reset Grok Bot's computer from settings. If a feature is missing, updating the computer may enable it.
3. Connect accounts and create bots.
   1. During setup, tell it what you're using it for and connect your services. Options include Gmail, Google Drive and Sheets, Slack, and Dropbox.
   2. Start with a core few accounts and add more over time.
   3. Create a separate bot for each category of work instead of one long conversation.
   4. Give each bot a description. You can also rename it, change its icon, and configure its voice.
   5. Delete bots that are not useful enough to keep.
4. Build a chief of staff bot.
   1. Send general requests to the chief of staff, which delegates to the right specialist bot.
   2. Set up a morning brief. Mine arrives at 7:00 a.m. local time wherever I am (it uses my calendar to know my location) and includes the date, the weather including dew point, my calendar in a format I refined until I liked it, and my Grok Bot usage.
   3. Ask the bot for more morning brief ideas. Suggestions I received included calendar conflict callouts, a first-meeting prep line, a kids-only line, top three Todoist items, expiring credits and travel, and a one-line fun fact.
   4. Have the chief of staff review your to-do list (mine is Todoist, connected through its API) once a day, suggest one task it can make progress on, and get your approval before starting. Reply directly to its suggestion so it has context.
5. Build a recruiter bot.
   1. Name a bot Recruiter. It offered options; I chose outreach and follow-ups, on LinkedIn.
   2. Give it the outreach plan. Mine: find people currently working as executive assistants in the Columbus metro area and send connection requests with a note describing the job and compensation and asking for referrals.
   3. Throttle daily connection requests.
   4. Turn on "route traffic through this computer" in settings so the agent's traffic comes from your own connection. With it off, LinkedIn flagged my account as suspicious after about 24 hours and warned it might disable it.
   5. Alternatively, run outreach through Dripify, a LinkedIn outreach tool recommended by my friend Dylan Scroggins, who does a lot of recruiting. I gave the bot a screenshot of the LinkedIn warning and told it to set up Dripify and move all candidate outreach there. It created the account (handing control to me only for the password), paid for the trial through Link, carried over the outreach cadence, and started recruiting.
   6. Ask for a daily update. Dripify allows 20 invites per day. On the day I recorded, the bot had sent 20 of 20 invites that day and contacted 116 people; 16 accepted and 12 replied. It tells me when I need to reply and sends the job description to anyone who asks.
6. Build a buy, sell, and returns bot.
   1. Connect your email, which holds your purchase, travel, and project history.
   2. Use it to track purchases, monitor items you're selling (for example, an eBay listing), and handle returns.
   3. When it needs to log in somewhere and hits two-factor authentication, it flags action needed. Click take over, log in on Grok Bot's computer, then click "I'm done, continue" so the bot finishes the task.
   4. Share specific logins (such as Amazon and eBay) through Grok Bot's 1Password integration, which creates a shared vault for only the logins you move into it.
7. Build Spam Hunter.
   1. Connect your work email.
   2. Describe what counts as obvious spam (for me, many podcast pitches and vendor emails).
   3. Ask it to start cautious and increase aggressiveness over time.
   4. Schedule it every weekday at 7:30 a.m., 11:00 a.m., and 3 p.m.
   5. Have it study the spam you have already marked.
   6. Create a Gmail label called Spam Hunter. On each run, the bot archives suspected spam and applies the label.
   7. Review the label about every other day for legitimate emails caught by mistake, then tell the bot to move reviewed emails to spam.
   8. When you mark something as spam that the bot missed, it recognizes the miss and learns from it.
8. Build a credit card points and travel bot.
   1. Give it every card you hold, your point balances, and screenshots of each card's bonus categories and rewards.
   2. Have it send a monthly message listing credits and rewards with what remains and when they expire. My Chase Sapphire Reserve credits include Chase Travel, dining, StubHub, Southwest, and shopping credits that reset quarterly, every 6 months, or annually.
   3. Ask which card to use for which spending category. I removed my Amex because I rarely use it; the result was the Chase Sapphire Reserve for specific categories and my X Money card (3% cash back at the time) for everything else.
   4. Ask about travel perks on the spot, such as which airport lounges you can access with your cards (I have Priority Pass through the Sapphire Reserve).
9. Build contacts, calendar, and medical admin bots.
   1. Connect the calendar and contacts bot to both. Photograph a business card to add the person to contacts.
   2. Load health, dental, and vision insurance details into a medical admin bot by photographing insurance cards front and back.
   3. Have it track HSA receipts for reimbursement and help process claims.
   4. Give it access to your calendar and shared family calendar so it records everyone's dental, doctor, vision, and annual checkup appointments and flags anyone falling behind.
   5. Use its record to answer health insurance application questions about each family member's last doctor visit, or have it fill out the application.

## Decision rules

- If an agent costs more time than it saves, stop using it or switch tools.
- If you're starting out, connect a core few accounts before adding more.
- If work falls into a distinct category, give it its own bot.
- If a request is general, send it to the chief of staff bot.
- If the chief of staff proposes working on a task, it must get approval before starting.
- If a site flags your agent as suspicious, turn on "route traffic through this computer," or move the work to a dedicated tool such as Dripify.
- If a feature is missing, update Grok Bot's computer.
- If a bot hits a login or two-factor prompt, take over, log in, and click "I'm done, continue" without doing the task yourself.
- If a bot needs a login, share only that login through a 1Password shared vault.
- If you receive any real volume of spam, make Spam Hunter your first bot.
- If you rarely use a credit card, remove it from the card recommendations to keep them simple.

## Common mistakes

- **Maintaining a fragile open-source agent.** My OpenClaw integrations kept breaking, and fixing them cost more time than the agent saved. Fix: use a maintained commercial agent.
- **Spending more time configuring than using.** Many people on social media tinker endlessly. Fix: keep only bots that return more time than they take.
- **One giant conversation with one bot.** Fix: separate bots for separate categories of work, with a chief of staff routing requests.
- **Connecting every account at once.** Fix: start with a core few.
- **Agent traffic coming from a data center.** Sites like LinkedIn, Apple, and Amazon increasingly flag or block it. Fix: route traffic through your own computer.
- **Expecting everything to work the first time.** Some tasks fail, such as a login blocked by two-factor authentication. Fix: take over the bot's computer to log in, then hand control back.
- **Sharing all your logins.** Fix: share specific logins through a 1Password shared vault.
- **Forgetting credit card credits and perks.** Credits reset on different schedules and are easy to miss. Fix: a monthly expiring-credit reminder from a bot that knows all your cards.
- **Losing track of family appointments.** Fix: a medical admin bot that tracks everyone's checkups from your calendars.

## Questions and answers

**Why did you stop using OpenClaw?**
Its integrations kept breaking, and I spent more time logging into my Mac Mini to restart things and redo connections than it saved me. Commercial agents like Grok Bot cost money but are maintained and much easier to use.

**How does Grok Bot stay in sync between my phone and computer?**
All the work runs on a dedicated virtual computer in the cloud, not on your device. Whether I use my phone, desktop, or laptop, I see the same bots, chat history, and capabilities.

**Should I use one AI agent bot or several?**
Several. I create a separate bot for each category of work and a chief of staff bot that routes general requests to the right one. The bots share logins and can hand tasks to each other.

**What should go in an AI morning brief?**
Mine includes the date, the weather with dew point, my calendar, and my Grok Bot usage, delivered at 7:00 a.m. local time wherever I am. You can ask the bot for more ideas, such as calendar conflict callouts or your top to-do items.

**Can an AI agent recruit candidates on LinkedIn?**
Yes, with care. My recruiter bot searched LinkedIn for executive assistants in the Columbus area and sent connection requests, but LinkedIn flagged my account after about 24 hours. Routing traffic through my own computer, or running outreach through Dripify, solved it. It has contacted 116 people, with 16 accepts and 12 replies.

**How do I stop websites from flagging my AI agent?**
Turn on Grok Bot's "route traffic through this computer" setting so traffic comes from your own internet connection instead of a data center. If the option is missing, update Grok Bot's computer.

**Is it safe to connect my email to an AI agent?**
It's a trade-off. I'm more comfortable with commercial software because the company has something to lose and the product has been tested by a very large number of users. I share other logins case by case through a 1Password shared vault.

**How can an AI agent filter spam in Gmail?**
My Spam Hunter bot runs every weekday at 7:30 a.m., 11:00 a.m., and 3 p.m., archives suspected spam under a Gmail label, and learns from what I correct. I review the label about every other day; so far it hasn't caught any legitimate email.

**How can an AI agent help with credit card rewards?**
Give it all your cards, balances, and bonus categories. Mine sends a monthly list of expiring credits, tells me which card to use for each category, and knows my travel perks, like Priority Pass lounge access through my Sapphire Reserve.

**How can an AI agent help with family medical admin?**
I photograph insurance cards to store the details, and the bot tracks HSA receipts, helps with claims, and uses our calendars to make sure everyone keeps up with dental, doctor, and vision checkups. It can also answer insurance application questions about each person's last doctor visit.

**Are there alternatives to Grok Bot?**
Muse from Meta has access to Instagram, Facebook, and Facebook Marketplace. Instinct is another option that I think is invite-only right now. They have similar capabilities.

## Video timestamps

- 00:00 Intro: why I stopped using OpenClaw
- 01:23 Why I switched to a commercial agent
- 03:13 Set up Grok Bot and its virtual computer
- 06:24 Connect your accounts and create one bot per job
- 09:08 Build a chief of staff and a morning brief
- 14:34 Automate recruiting outreach
- 22:15 Track purchases, sales, and returns
- 27:20 Hunt down spam automatically
- 30:35 Maximize credit card points and travel perks
- 35:09 Contacts, calendar, and family medical admin
