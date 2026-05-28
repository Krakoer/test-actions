import assert from 'node:assert/strict';
import { describe, it } from 'node:test';
import { add, sum } from '../dist/index.js';

describe('add', () => {
  it('adds integers', () => {
    assert.equal(add(2, 3), 5);
  });

  it('adds floats', () => {
    assert.equal(add(0.1, 0.2), 0.30000000000000004);
  });
});

describe('sum', () => {
  it('sums multiple values', () => {
    assert.equal(sum(1, 2, 3, 4), 10);
  });

  it('returns 0 for no arguments', () => {
    assert.equal(sum(), 0);
  });
});
