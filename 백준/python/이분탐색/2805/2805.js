const readline = require('readline');
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let input = []; // 입력을 저장할 배열

rl.on('line', (line) => {
    input.push(line); // 입력받은 각 줄을 input 배열에 추가

    // 입력이 두 줄 다 들어오면 처리
    if (input.length === 2) {
        let [N, M] = input[0].split(" ").map(Number); // 첫 줄의 값을 N과 M으로 분리
        let array = input[1].split(" ").map(Number).sort((a,b)=>a-b);  // 두 번째 줄의 값을 숫자 배열로 변환

        let start = 0;
        let end = array[array.length-1];
        let answer = 0;

        while(start <= end){
          let sum = 0;
          let mid = Math.floor((start + end) / 2);

          for(let i = 0; i<array.length; i++){
            if(array[i] < mid){
              continue;
            }
            sum += array[i]-mid;
          }
          if(sum >= M){
            if(mid > answer){
              answer = mid;
            }
            start = mid + 1;
          }else{
            end = mid - 1;
          }
        }
        console.log(answer);
        rl.close(); // 입력 종료
    }
}).on('close', () => {
  process.exit(0);
});