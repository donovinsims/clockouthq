# Track Google Business Profile website visits

- Title type: editorial
- Author / handle: @noahiglerSEO
- Original URL: https://x.com/noahiglerSEO/status/2065474223905128605
- Post ID: 2065474223905128605
- Published: 2026-06-12
- Captured: 2026-11-09
- Topics: local-seo, google-business-profile, measurement
- Status: reviewed
- Source format: user-supplied X bookmark export
- Coverage and access limits: Complete supplied post text. The live post was not checked. Attached media was not reviewed.

## Why Donovin saved it

Not specified.

## Source material

Original post text from the supplied export.

Someone finds you in the map pack, clicks through to your website, and books a job.

Almost no home service company TRACKS that path correctly, which means the channel that drove the job gets zero credit for it.

Here's why it breaks:

That click from your Google Business Profile to your site lands in "direct" traffic in your analytics, the same bucket as someone who typed your web address in by hand.

So your profile looks dead and your SEO looks weak, when the profile is the exact thing that sent you the customer. You end up making budget decisions off numbers that are lying to you.

The fix takes about ten minutes.

> Grab the website link inside your Google Business Profile dashboard
> Add a UTM tag to it, something like ?utm_source=gbp&utm_medium=organic
> Now every click off your profile shows up tagged in GA4 instead of hiding in direct
> Confirm it's firing in Google Tag Manager so you know the data's clean

I also heavily recommend training your front desk to ask every caller how they found you. Software misses things, tracking breaks, people search on one device and call from another. A human asking "how'd you hear about us" is still one of the most accurate data points you've got.

Track the profile right and you'll almost always find it's pulling more than you thought.

## What the author recommends

The author proposes adding UTM parameters to the profile website link and asking callers how they found the business to cover gaps in digital attribution.

## Codex assessment

The tag gives analytics a source label for observed visits. The post gives no measured improvement and overstates how consistently untagged visits appear as direct. Use [Google Analytics campaign tagging guidance](https://support.google.com/analytics/answer/10917952) for parameter naming and verify the analytics report itself.

## Potential Clockout application

Extend the local SEO baseline for a client who already has authorized analytics. Report profile interactions, tagged website visits, inquiries, and booked jobs as separate measures.

## Possible test

Open the approved tagged URL in a test session and verify that analytics records the expected campaign. Check that a redirect preserves the parameters and that the destination still works.

## Follow-up evidence or decision

None.
