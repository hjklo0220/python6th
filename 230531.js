
////화씨 구하기
//var cels = parseFloat(prompt("섭씨 입력 : "));
//var farn = cels * (9 / 5) + 32;
//
//document.write("화씨 : " + farn)

////비교 연산자
//var num1 = 20;
//var num2 = 10;
//var num3 = "10";
//var num4 = 20;
//var num5 = 15;
//
//console.log(num1 > num2, num1, '>', num2);
//console.log(num1 >= num2, num1, '>=', num2);
//console.log(num1 < num2, num1, '<', num2);
//console.log(num1 <= num2, num1, '<=', num2);
//
//console.log(num1 == num4, num1, '==', num4);
//console.log(num1 != num4, num1, '!=', num4);
//
//console.log(num1 === num3, num1, '===', num3);  //타입과 함께 비교
//console.log(num2 === num3, num2, '===', num3);
//console.log(num2 == num3, num2, '==', num3);    // 문자열'10'과 숫자 10이어도 true 나옴 그래서 ===추가됨
//
//console.log('num1 > num2 && num1 < num5', num1 > num2 && num1 < num5);  //and 논리 연산자
//console.log('num1 > num2 || num1 < num5', num1 > num2 || num1 < num5);  //or
//console.log('num1 > num2 && num1 < num5', num1 > num2 && !(num1 < num5));   //not !


////조건문
//var num1 = parseInt(prompt("첫번째 숫자 입력 : "));
//var num2 = parseInt(prompt("두번째 숫자 입력 : "));
//
//if(num1 > num2) {
//    console.log("큰 수 1: " + num1);
//}
//if(num1 < num2) {
//    console.log("큰 수 2: " + num2);
//}
//if(num1 == num2) {
//    console.log("같은 수")
//}
//
//if(num1 > num2) {       //나눠서 짜는거보다 묶어서 사용하는 것이 조금더 효율적 가독성도 높아짐, 하지만 위와같이 나눠써야 할 때도 있음
//    console.log("큰 수 num1 : " + num1);
//} else if(num1 < num2) {
//    console.log("큰 수 num2" + num2);
//} else if(num1 == num2) {
//    console.log("같은 수")
//}
//
//if(num1 > num2) {
//    console.log("큰 수 num1 : " + num1);
//} else if(num1 < num2) {
//    console.log("큰 수 num2" + num2);
//} else (num1 == num2) {     // 예외조건에 대한 대비 else
//    console.log("같은 수")
//}


// 모음 자음 구별하기
var letter = prompt("Enter a letter : ");
letter = letter.toLowerCase();

if(letter =='a' || letter == 'e' || letter == 'i' || letter == 'o' || letter == 'u'){
    console.log('Vowel');
} else {
    console.log('Consonant');
}

