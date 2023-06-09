//출력
document.write('hello world2');
document.write("<h1>Welcome to JS Program</h1>");
document.write("<h2>Welcome to JS Program</h2>");

console.log("Welcome JS Program");
console.info("Welcome JS Program"); //기본
console.warn("Welcome JS Program");
console.error("Welcome JS Program");

//alert('Welcome JS Program');
//var a = prompt('Welcome JS Program');
//console.log(a);

//데이터 타입
console.log(123, typeof 123);    // number
console.log(123.5, typeof 123.5);  // number
console.log('123', typeof '123');  // string
console.log(true, typeof true);   //boolean
console.log(false, typeof false);  //boolean

var car;
console.log(typeof car);    //undefined - 아무것도 없음
var car = ""
console.log(typeof car);    //string
console.log(isNaN());       //NaN - 잘못된 입력을 받았음을 나타내는 기호
var person = {
    firstName : 'John',
    lastName: 'Doe',
    age : 50,
    eyeColor : "blue"
    };
console.log(typeof person, person); //object
person = null; //null - '값 없음' 이라는 값이 있음
console.log(typeof person, person); //object

//문자열 연결
var name = "홍길동";
var age = 29;
var cgpa = 3.92;
var linebreak = "<br/>"

document.write("이름 : " + name + linebreak);
document.write("이름 : " + age + linebreak);  // age 문자로 변형됨 (js의 특징)
document.write("이름 : " + cgpa + linebreak);

var lastName = "홍";
var firstName = "길동";
var fullName = lastName + firstName;

console.log(fullName);
console.log("Today is" + " a " + "beautiful day");
console.log("My name is " + fullName);

var num1 = 20;
var num2 = 30;
var sum = num1 + num2;
console.log(num1 + num2);       // 50
console.log("" + num1 + num2);  // 2030 덧셈기호로 문자에 덧셈해서 문자열로 바꿔버림 -js특징
console.log(num1 + " + " + num2 + " = " + sum);

/*
//문자열 함수 실습
var text = prompt("Enter your name : ");
document.write("Your name : " + text + "<br>");

var len = text.length;      // length: 문자열 객체의 프로퍼티
document.write("Number of characters : " + len + "<br>");

document.write(text.charAt(2) + "<br>");    // 인덱스 2 출력 charAt() : 메소드(객체에 포함된 함수)

document.write(text.toUpperCase() + "<br>") //대문자
document.write(text.toLowerCase() + "<br>") //소문자
*/

var text1 = "hi ";
var text2 = "bye";
var text3 = text1.concat(text2);
var text4 = text1 + text2;  //위와 같음
document.write(text3 + "<br>");
document.write(text4 + "<br>");

var text5 = "hello";
var result = text5.slice(0,-2);  // slice : 문자열 자르기 함수
document.write(result + "<br>");


//데이터 타입 변환
var num = "20";
num = num.toString();
console.log(typeof num); // typeof : 예약어
var number = 20
console.log(typeof number);
number = toString(20);
console.log(typeof number);

var x = 2.56789
console.log(x.toFixed(1), typeof x.toFixed(1));  // toFixed : 소수점 첫째자리까지 표현 (둘째자리에서 반올림)
console.log(x.toFixed(2));

console.log(x.toPrecision(1), typeof x.toPrecision(1)); // toPrecision : 소수점 첫째자리에서 반올림
console.log(x.toPrecision(2));

console.log(Number(true));
console.log(Number(false));
console.log(Number("10"));
console.log(Number(" 10 "));
console.log(Number("10.25"));

/*
//연산자
var num1 = parseInt(prompt("Enter First number : "));
var num2 = parseInt(prompt("Enter Second :  number"));
var lineBreak = "<br/>";

var result = num1 + num2;
document.write("the sum is : " + result + linebreak);

result = num1 - num2;
document.write("the sub is : " + result + linebreak);

result = num1 * num2;
document.write("the mul is : " + result + linebreak);

result = num1 / num2;
document.write("the div is : " + result + linebreak);

result = num1 % num2;
document.write("the remainder is : " + result + linebreak);
*/

// 삼각형 넓이 구하기
var base = parseFloat(prompt("Enter 밑변 : "));
var height = parseFloat(prompt("Enter 높이 : "));

var area = base * height * 0.5;

document.write("넓이 : " + area);



