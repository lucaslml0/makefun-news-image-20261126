import { copyFileSync, mkdirSync } from "node:fs";
import { join } from "node:path";

// Copy the pre-drawn front page into the output directory.
const outDir = process.env.MAKEFUN_OUTPUT_DIR ?? "/output";
mkdirSync(outDir, { recursive: true });
copyFileSync(new URL("./entry.png", import.meta.url), join(outDir, "entry.png"));
