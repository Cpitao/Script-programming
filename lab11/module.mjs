/** Operation class allowing to add two numbers */
export class Operation {
    /** Initialize Operation class with two integer arguments
     * @param {int} x - first number
     * @param {int} y - second number
     */
    constructor(x, y) {
        this.x = x;
        this.y = y;
    }

    /** Return sum of parameters passed in constructor */
    sum() {
        return this.x+this.y;
    }
}
