# TypeScript Master Reference

This folder contains 37 small TypeScript reference files.

Each file focuses on one topic.

## Check Node.js

```bash
node -v
npm -v
```

## Install dependencies

From this folder, run:

```bash
npm install
```

## Run one TypeScript file

```bash
npx ts-node 01_console_output.ts
```

or:

```bash
npx ts-node 31_oop_class_and_object.ts
```

## Compile TypeScript

```bash
npx tsc --noEmit
```

## Playwright example

File `36_playwright_basic_test_example.spec.ts` is a reference example.
To run Playwright tests properly, create a Playwright project:

```bash
npm init playwright@latest
```

## Recommended learning order

Start with:

1. 03_variables.ts
2. 04_basic_types.ts
3. 10_arrays.ts
4. 12_objects.ts
5. 14_array_of_objects.ts
6. 18_functions.ts
7. 30_async_await.ts
8. 31_oop_class_and_object.ts
9. 35_page_object_login_example.ts
10. 36_playwright_basic_test_example.spec.ts
