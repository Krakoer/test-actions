/** Add two numbers. */
export function add(a: number, b: number): number {
  return a + b;
}

/** Sum any number of values. */
export function sum(...numbers: number[]): number {
  return numbers.reduce((total, n) => total + n, 0);
}
