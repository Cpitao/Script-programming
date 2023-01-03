import {Operation} from "./module.mjs";

let USAGE = "node index.mjs arg1 arg2";
if (process.argv.length < 4)
{
    throw new Error(USAGE);
}

var x = parseInt(process.argv[2]);
var y = parseInt(process.argv[3]);

const operation = new Operation(x, y);
console.log(operation.sum());
