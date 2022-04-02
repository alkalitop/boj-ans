stdin=require('fs').readFileSync('./dev/stdin').toString().trim().split('\n');input=_=>(stdin.splice(0, 1)+'').trim();
