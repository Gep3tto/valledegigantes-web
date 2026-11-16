# AFER Greens / Valle de Gigantes site

Brand, audience and tone are in [PRODUCT.md](PRODUCT.md). Colours, type and components are in [DESIGN.md](DESIGN.md); it wins over any skill or reference. Text research is in [mockups/RESEARCH.md](mockups/RESEARCH.md); the four directions are `mockups/a` to `d`.

## How design work runs here

1. **References first.** Screenshots go in `refs/`, sorted by type (see [refs/README.md](refs/README.md)). The `inspo` MCP server finds real sites; save the captures that matter. References set the quality bar; combine their direction, never copy one element 1:1.
2. **One section per prompt.** Hero, product cards, story, certifications, contact: build and finish one before starting the next.
3. **Real assets.** Use the farm's own photos and real product data. No stock stand-ins, no invented figures.
4. **Score before showing.** A fresh-context agent that sees only a 390px screenshot of the section next to its references scores composition, legibility, colour and detail out of 10. The bar is 8 on each; the building agent's own score never counts; two critic rounds at most, then report the scores as they stand.
5. **Stills before motion.** Screenshots get approved before any animation or video is built.

## Ban list

Never use these unless DESIGN.md calls for them (Fraunces is the brand face, not a decorative serif):

- eyebrow labels above headings
- monospace uppercase text
- serif faces other than Fraunces
- beige as a default background; purple gradients
- 01 / 02 / 03 counters
- glowing orbs, shockwave rings, decorative particles
- em dashes in site copy

## Checks

- Every section is checked at 390px width before it is called done.
- Run `break-ui` on product cards: long Spanish and English product names, large weights and prices.
- `cook` is for one flagship piece at a time, always with a hard time cap in the brief.
