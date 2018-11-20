

function processData(input) {
    //Enter your code here
    input = input.split('\n')
    let x = [],
        y = []

    for (let i = input.length; i-- > 0;) {
        let v = input[i].split(' ').map(Number)
        x[i] = v[0]
        y[i] = v[1]
    }

    function linearRegression(x, y, z) {
        let n = x.length,
            sx = 0,
            sy = 0,
            sxx = 0,
            sxy = 0,
            syy = 0

        for (let i = n; i-- > 0;) {
            sx += x[i]
            sy += y[i]
            sxx += Math.pow(x[i], 2)
            sxy += x[i] * y[i]
            syy += Math.pow(y[i], 2)
        }

        let b = (n * sxy - sx * sy) / (n * sxx - Math.pow(sx, 2)),
            a = (1 / n) * sy - b * (1 / n) * sx

        return [a, b]
    }

    function regressionEquation(a, b, x) {
        return b * x + a
    }

    console.log(regressionEquation(...linearRegression(x, y), 80).toFixed(3))
}

// custom input test:
// processData(`95 85
// 85 95
// 80 70
// 70 65
// 60 70`)