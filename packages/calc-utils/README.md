# @krakoer/calc-utils

Small math helpers used in the supply-chain attack demo.

## Install from a GitHub release

Replace `VERSION` with a release tag (for example `v1.0.0`):

```bash
npm install https://github.com/Krakoer/test-actions/releases/download/VERSION/krakoer-calc-utils-1.0.0.tgz
```

With pnpm:

```bash
pnpm add https://github.com/Krakoer/test-actions/releases/download/VERSION/krakoer-calc-utils-1.0.0.tgz
```

The tarball name matches `npm pack` output: scoped `@` and `/` become `-`.

## Usage

```js
import { add, sum } from '@krakoer/calc-utils';

console.log(add(2, 3)); // 5
console.log(sum(1, 2, 3, 4)); // 10
```

## Development

```bash
pnpm --filter @krakoer/calc-utils test
pnpm --filter @krakoer/calc-utils build
```

Releases are published by the [Release workflow](../../.github/workflows/release.yml) when a `v*` tag is pushed or the workflow is run manually.
