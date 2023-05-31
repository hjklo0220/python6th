
////화씨 구하기
//var cels = parseFloat(prompt("섭씨 입력 : "));
//var farn = cels * (9 / 5) + 32;
//
//document.write("화씨 : " + farn)

//비교 연산자
var num1 = 20;
var num2 = 10;
var num3 = "10";
var num4 = 20;
var num5 = 15;

console.log(num1 > num2, num1, '>', num2);
console.log(num1 >= num2, num1, '>=', num2);
console.log(num1 < num2, num1, '<', num2);
console.log(num1 <= num2, num1, '<=', num2);

console.log(num1 == num4, num1, '==', num4);
console.log(num1 != num4, num1, '!=', num4);

console.log(num1 === num3, num1, '===', num3);  //타입과 함께 비교
console.log(num2 === num3, num2, '===', num3);
console.log(num2 == num3, num2, '==', num3);    // 문자열'10'과 숫자 10이어도 true 나옴 그래서 ===추가됨

console.log('num1 > num2 && num1 < num5', num1 > num2 && num1 < num5);  //and 논리 연산자
console.log('num1 > num2 || num1 < num5', num1 > num2 || num1 < num5);  //or
console.log('num1 > num2 && num1 < num5', num1 > num2 && !(num1 < num5));   //not !




