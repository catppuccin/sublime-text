#!/usr/bin/env deno run --allow-write=.

import {
  flavors,
  flavorEntries
} from "https://deno.land/x/catppuccin@v1.1.1/mod.ts";

// Load color-scheme.json
import colorScheme from "./color-scheme.json" with { type: "json" };

for (const [name, flavor] of flavorEntries) {
  // Add a "variables" field with the colors for each theme
  colorScheme.variables = Object.fromEntries(Array.from(Object.entries(flavor.colors)).map(([name, color]) => {
    return [name, color.hex];
  }));

  // Write out the new JSON to build/
  const jsonText = JSON.stringify(colorScheme, null, 4);
  Deno.writeTextFileSync(`build/Catppuccin ${flavor.name}.sublime-color-scheme`, jsonText + "\n");
}
