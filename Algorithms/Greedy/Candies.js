'use strict';

const fs = require('fs');

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', inputStdin => {
    inputString += inputStdin;
});

process.stdin.on('end', function() {
    inputString = inputString.replace(/\s*$/, '')
        .split('\n')
        .map(str => str.replace(/\s*$/, ''));

    main();
});

function readLine() {
    return inputString[currentLine++];
}

// Complete the candies function below.
function candies(n, arr) {
    let candiesTemp = [],
        count = 0;
    for (let i = 0, currentNumberOfCanies = 1; i < n; i += 1) {
        if (i > 0) {
            currentNumberOfCanies = arr[i - 1] < arr[i] ? currentNumberOfCanies + 1 : 1;
        }
        candiesTemp.push(currentNumberOfCanies)
    }
    for (let i = n - 1, currentNumberOfCanies = 1; i >= 0; i -= 1) {
        if (i < n - 1) {
            currentNumberOfCanies = arr[i] > arr[i + 1] ? currentNumberOfCanies + 1 : 1;
        }
        count += currentNumberOfCanies > candiesTemp[i] ? currentNumberOfCanies : candiesTemp[i];
    }

    return count;
}
function main() {
    const ws = fs.createWriteStream(process.env.OUTPUT_PATH);

    const n = parseInt(readLine(), 10);

    let arr = [];

    for (let i = 0; i < n; i++) {
        const arrItem = parseInt(readLine(), 10);
        arr.push(arrItem);
    }

    const result = candies(n, arr);

    ws.write(result + '\n');

    ws.end();
}
