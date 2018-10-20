'use strict';

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', inputStdin => {
    inputString += inputStdin;
});

process.stdin.on('end', _ => {
    inputString = inputString.trim().split('\n').map(string => {
        return string.trim();
    });
    
    main();    
});

function readLine() {
    return inputString[currentLine++];
}
    
/*
 * Complete the vowelsAndConsonants function.
 * Print your output using 'console.log()'.
 */

    function vowelsAndConsonants(s) {
        let s1 = new Set(['a', 'e', 'i', 'o', 'u']);
        let s2 = new Set(['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']);
        var i, j;
        for (i = 0; i <= s.length; i++) {
            if (s1.has(s[i])) {
                console.log(s[i]);
            }

        }
        for (j = 0; j <= s.length; j++) {
            if (s2.has(s[j])) {
                console.log(s[j]);
            }

        }
    }



function main() {
    const s = readLine();
    
    vowelsAndConsonants(s);
}