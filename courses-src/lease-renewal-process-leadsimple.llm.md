# Build a Lease Renewal Process in LeadSimple, Step by Step

- Author: Peter Lohmann (property management operator; owner of RL Property Management, Columbus, Ohio)
- Published: 2026-10-30
- Video: https://www.youtube.com/watch?v=rphTnIq3SXQ
- Course page: https://peterlohmann.com/courses/lease-renewal-process-leadsimple/
- Topics: lease renewal process, LeadSimple, AI process builder, property management workflow software, process stages, custom fields, e-signature, autopilot rules, Buildium
- Related course: https://peterlohmann.com/courses/property-management-processes-systems/

## Summary

Every core process at my property management company (move-ins, move-outs, new owners, and lease renewals) runs through LeadSimple, a workflow tool that integrates with our property management software. We manage about 700 doors in Columbus, Ohio, on Buildium; LeadSimple also integrates with AppFolio, Rentvine, and Rent Manager. In this live, unscripted build, I create a lease renewal process from scratch using LeadSimple's AI-assisted process builder: I describe the process in plain language, let the AI draft the stages, steps, custom fields, and emails, fix what it gets wrong, add outcome stages for reporting, connect e-signature, test the process, and set autopilot rules that start it automatically about 90 days before each lease expires.

## Key terms

- **Process:** a repeatable workflow in LeadSimple, run as a separate instance for each property, tenant, or owner.
- **Stage:** a major milestone in a LeadSimple process.
- **Step:** an individual action inside a stage, such as a to-do, email, phone call, e-signature request, change stage, or create process.
- **Change stage step:** a step that moves the process to another stage, either manually or automatically.
- **Create process step:** a step that starts another process, such as starting the move-out process when a tenant won't renew.
- **Automatic vs. manual:** each step can run automatically or wait for a person. During a build, I keep outbound emails and process triggers on manual so nothing goes to a real tenant by accident.
- **Custom field:** process-specific data, such as lease expiration date or new rental rate. A step can require a custom field before it can be completed.
- **Completed and canceled stages:** end stages that record the outcome of each process instance.
- **Autopilot:** rules that start a process automatically when conditions are met.
- **Legacy view:** LeadSimple's previous process editor, still available and kept in sync with the new editor.

## Prerequisites

- A LeadSimple account connected to your property management software (I use Buildium).
- Existing roles in LeadSimple, such as leasing assistant, leasing lead, and property manager.
- An existing move-out (lease ending) process in LeadSimple for non-renewals to hand off to.
- A lease renewal document template if you will use LeadSimple's e-signature.

## Step-by-step

1. Create the process.
   1. In LeadSimple, go to Processes and click Create new.
   2. Name the process (I used "PL demo lease renewal"). The item name can be left for later.
   3. Confirm the category. LeadSimple auto-detected the lease renewal category from the name.
   4. Click Set up workflow, then Set up with a guide.
2. Describe the process in plain language. The guided setup accepts pasted checklists, meeting notes, or attached documents; messy is fine. My lease renewal process description:
   1. Start 90 days before the current lease expires.
   2. Email the resident to ask whether they want to renew.
   3. If they don't want to renew, start the move-out process for that unit.
   4. If they want to renew, determine the renewal rent with a market rent analysis.
   5. Confirm the property owner wants to renew and approves the amount. Owners want to know before a renewal because they may want to sell or move into the property.
   6. If the owner approves, email the resident a renewal offer.
   7. If the resident accepts, send the lease renewal for e-signature.
   8. If the resident declines or counters, work with the owner and tenant on price until everyone agrees, then send for e-signature.
   9. If all tenants want to go month-to-month and the owner agrees, move to a month-to-month stage.
   10. After the tenant signs, countersign, then send the signed renewal to all parties, including the owner.
   11. Upload the renewal to Buildium and Dropbox.
   12. Update the Buildium lease terms with the new rent and any changed terms, such as the lease end date.
   13. Charge the rental owner the lease renewal fee in Buildium.
   14. For month-to-month, update the Buildium lease terms with the new rent and any changed terms.
3. Analyze and map roles.
   1. Click Analyze material.
   2. Map the roles the AI finds to existing roles (mine: leasing assistant, leasing lead, property manager).
   3. Review the setup summary; any answer can still be changed.
4. Build the workflow with AI.
   1. Click Build workflow. The AI process assistant appears on the right.
   2. Accept the stages. Mine: renewal outreach, non-renewal handoff, price and approve, offer and negotiate, month-to-month, lease execution, and records and closeout.
   3. Accept the steps for each stage. Renewal outreach got: confirm lease expiry, ask renewal intent, and record resident choice.
   4. Let the AI build every stage before editing anything, then review each stage.
   5. If the AI can't identify an existing process to start (it couldn't find my move-out process, named "Reorg lease ending process"), decline its proposal and add the step manually: Add step, choose Create process, and set the target to your move-out process.
   6. Keep outbound emails and process triggers on manual during the build; switch them to automatic when the process goes live.
5. Add outcome stages. Create one end stage per outcome so you can report on renewal rate by stage name:
   1. Completed: lease renewed.
   2. Completed: month-to-month.
   3. Canceled: tenant is vacating (the tenant may not have moved out yet). This could also be a completed stage; I placed it under canceled.
   4. Canceled: other (for example, the property is demanaged mid-renewal).
6. Review steps and generate emails.
   1. Confirm lease expiration populates the lease expiration date custom field.
   2. For the ask renewal intent email step, click Generate with AI. The AI wrote an email asking the resident to reply with one of three options (renew my lease, move out at the end of my lease, or I'm interested in discussing other options) and filled in the mail merge tags, saving about 10 minutes.
   3. The AI created these custom fields: new rental rate, lease signing date, tenant renewal choice, owner renewal approval, owner month-to-month approval, lease expiration date, market rent, and resident offer response (accepted, declined, or counter offer).
7. Route stages automatically.
   1. Tell the AI assistant: in the renewal outreach stage, if the tenant renewal choice custom field says the resident does not want to renew, automatically move to the non-renewal handoff stage. Accept the proposed change stage step.
   2. Do the same for renewals: if the resident wants to renew, automatically move to the price and approve stage.
   3. Adjust assignees as needed. The AI assigned the first steps to the leasing assistant and others to the process owner; any step can be assigned to a specific person or role.
8. Configure price and approve.
   1. Determine market rent (manual step) and record it in the market rent field, shown only when the resident is renewing.
   2. Obtain owner approval by phone call.
   3. Set renewal rent, requiring the new rental rate custom field before the step can be completed.
   4. Add a change stage step to offer and negotiate, set to automatic.
   5. Note: steps that require a custom field have no step instructions. Normal to-do steps support step instructions, which appear as the step's content in the new view.
9. Configure offer and negotiate.
   1. Generate the renewal offer email with AI.
   2. Record the offer response (accepted, declined, or counter offer).
   3. Negotiate renewal terms, a step that appears only for declined or counter offer.
   4. Tell the AI: if the resident offer response is accepted, automatically move to the lease execution stage.
10. Configure lease execution.
    1. Set the send renewal for signature step (e-signature type) to use your lease renewal template, then set up its mail merge tags.
    2. Keep confirm resident signature and countersign renewal as checks, reordered as needed.
    3. Add a change stage step to records and closeout.
    4. LeadSimple's e-signature tool is under Signatures. Open a template, view the source PDF, and use Builder to place initial and signature fields for each signer. My company uses it for property management agreements and is testing it for leases.
11. Configure records and closeout.
    1. Distribute the executed lease. My company notifies the owner by email without attaching the lease.
    2. Archive renewal documents.
    3. Update Buildium lease terms.
    4. Change stage to Completed: lease renewed, set to automatic.
    5. Optionally add steps inside completion stages, such as emailing the owner.
12. Connect the month-to-month path.
    1. In renewal outreach, duplicate the renewal routing step, rename it "route confirmed month-to-month," and point it to the month-to-month stage.
    2. In the month-to-month stage (obtain owner approval, record month-to-month), point the final change stage step to Completed: month-to-month.
13. Check the workflow diagram (View diagram). Renewal outreach should branch to non-renewal handoff, month-to-month, or price and approve, which continues to offer and negotiate, lease execution, and records and closeout.
14. Test the process.
    1. Exit the builder and click Test process.
    2. Choose a due date and start the test.
    3. Complete required fields (the lease expiration date can be entered manually or pulled from Buildium with extra setup).
    4. Click through each stage to confirm its first step appears, then end the test.
15. Set up autopilot.
    1. In process settings, open Autopilot rules. Autopilot cannot be turned on while the process is in draft.
    2. Use LeadSimple's lease renewal autopilot template.
    3. Run it weekly at 6 a.m. (I prefer weekly to daily so the team can work in a rhythm).
    4. Start in the renewal outreach stage.
    5. Conditions: lease end date is less than 91 days in the future (to catch every lease, rather than exactly 90 days); active in PM software is true; current lease move-out date is empty.
    6. Exclude tenants already in: eviction, delinquency, the lease renewal process itself, lease break, lease ending, property de-management, collections, or cure.
    7. Save.
16. Review autopilot history. On a live process, the History tab shows the last 30 days of autopilot runs. On the Monday I recorded, our live lease renewal autopilot ran at 6:00 a.m. and created four lease renewal processes for four properties.

## Decision rules

- If the lease expires in less than 91 days, the tenant is active in the PM software, no move-out date is set, and the tenant is not in an excluded process, autopilot starts a lease renewal.
- If the resident does not want to renew, move to non-renewal handoff and start the move-out (lease ending) process.
- If the resident wants to renew, move to price and approve.
- If the resident and owner agree to month-to-month, move to the month-to-month stage, then to Completed: month-to-month.
- If the owner approves the renewal rent, move to offer and negotiate.
- If the resident accepts the offer, move to lease execution.
- If the resident declines or counters, negotiate with the owner and tenant until everyone agrees, then send for e-signature.
- If the renewal is signed and recorded, move to Completed: lease renewed.
- If the process is still being built, keep tenant emails and process triggers on manual.
- If a step needs data before it's done, require the custom field.

## Common mistakes

- **Editing before the AI finishes.** Let the AI build every stage first, then review, so it builds from its own complete plan.
- **Trusting the AI to find existing processes.** It may not locate your move-out process. Add the create process step manually.
- **Going automatic too early.** An automatic email or move-out trigger can reach a real tenant during testing. Keep them manual until the process is live.
- **One generic completed stage.** Separate completed and canceled stages by outcome so you can report on renewal rate from stage names.
- **Missing routes.** I forgot to route month-to-month. Check the workflow diagram for paths that don't connect.
- **Change stage pointing to the current stage.** The AI's month-to-month stage changed to itself; point it to the completion stage instead.
- **Starting renewals on exactly 90 days.** Use less than 91 days so a weekly autopilot run doesn't miss leases.
- **Starting renewals for tenants in conflicting processes.** Exclude eviction, delinquency, lease break, lease ending, de-management, collections, cure, and existing lease renewals.

## Questions and answers

**How do I build a lease renewal process in LeadSimple?**
Create a new process, choose Set up with a guide, describe your lease renewal process in plain language, map roles, and click Build workflow. The AI drafts stages, steps, custom fields, and emails. Then review each stage, add outcome stages, connect e-signature, test it, and set autopilot rules.

**What stages should a lease renewal process have?**
My build used renewal outreach, non-renewal handoff, price and approve, offer and negotiate, month-to-month, lease execution, and records and closeout, plus end stages: Completed: lease renewed, Completed: month-to-month, Canceled: tenant is vacating, and Canceled: other.

**When should the lease renewal process start?**
About 90 days before the lease expires. My autopilot rule starts it for any lease ending in less than 91 days, runs weekly at 6 a.m., and begins in the renewal outreach stage.

**Which tenants should be excluded from automatic lease renewals?**
I exclude anyone already in eviction, delinquency, a lease renewal, a lease break, lease ending, property de-management, collections, or a cure.

**Why use separate completed and canceled stages?**
They let you report on outcomes, including lease renewal rate, from the stage names alone. Each process instance ends in the stage that matches what happened.

**Can LeadSimple's AI write lease renewal emails?**
Yes. On an email step, click Generate with AI. It wrote my renewal-intent and renewal-offer emails, including mail merge tags, in seconds.

**How does LeadSimple route a resident to the right stage?**
Add a change stage step with a condition on a custom field, such as tenant renewal choice. I describe the rule to the AI assistant in plain English and it creates the step.

**Does LeadSimple have e-signature?**
Yes. It's under Signatures. You upload a template PDF and use Builder to place initial and signature fields for each signer. My company uses it for property management agreements and is working on moving our lease into it.

**What does the owner approval step look like?**
After determining market rent, the leasing team calls the owner to approve the renewal and the amount, then records the new rental rate in a required custom field.

**How do I know autopilot is working?**
Check the History tab on the live process. It shows 30 days of autopilot runs and which processes each run created.

## Video timestamps

- 00:00 Intro: why every process at my company runs in LeadSimple
- 01:33 Create the process
- 02:51 Describe your process in plain language
- 07:10 Let the AI build stages and steps
- 13:02 Tour the new editor and add completion stages
- 17:31 Review steps and write emails with AI
- 19:35 Route stages automatically
- 23:16 Price, offer, and e-signature
- 30:55 Close out and connect month-to-month
- 35:47 Test the process
- 37:34 Turn on autopilot
