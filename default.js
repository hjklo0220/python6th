
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


var name = "이승훈";
var age = 29;
var cgpa = 3.92;
var linebreak = "<br/>"

document.write("이름 : " + name + linebreak);
document.write("이름 : " + age + linebreak);  // age 문자로 변형됨 (js의 특징)
document.write("이름 : " + cgpa + linebreak);





