#!/usr/bin/env deno run --allow-write=.

import {
  flavors,
  flavorEntries
} from "https://deno.land/x/catppuccin@v1.1.1/mod.ts";

// Load color-scheme.json
import colorScheme from "./color-scheme.json" with { type: "json" };

function capitalize (word) {
  return word[0].toUpperCase() + word.slice(1);
}

for (const [name, flavor] of flavorEntries) {
  // Add a "variables" field with the colors for each theme
  colorScheme.variables = Object.fromEntries(Array.from(Object.entries(flavor.colors)).map(([name, color]) => {
    return [name, color.hex];
  }));

  // Write out the new JSON to build/
  const jsonText = JSON.stringify(colorScheme, null, 4);
  // Sublime Text uses the file name, e.g. "Catppuccin Frappe.sublime-color-scheme"
  //  to identify the color scheme.
  // This file name CANNOT change without breaking things for users
  Deno.writeTextFileSync(`build/Catppuccin ${capitalize(name)}.sublime-color-scheme`, jsonText + "\n");
}
