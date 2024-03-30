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
  // flavor.name has an uppercase version of name but it includes é for Frappe and I'm not ready for UTF-8 file names
  Deno.writeTextFileSync(`build/Catppuccin ${name.toUpperCase()}.sublime-color-scheme`, jsonText + "\n");
}
