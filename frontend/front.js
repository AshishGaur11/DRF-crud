console.log("hello world");

//  a = []
// let username = 'admin';
// let password = '12345';
// let auth = btoa(`${username}:${password}`);
//  var test;

//   const wesP = fetch("http://127.0.0.1:8000/" , {
// 	headers: {
// 		'Authorization': `Basic ${auth}`  
// 	}
// });
//    test = wesP
//   .then((response) => response.json())
//   .then((data) => {console.log(data); test = data;})
const val = [];
  //now we need to reade, create, update, delete using JS
(async function () {

  const response = await fetch("http://127.0.0.1:8000/snippets/");
  const joke = await response.json();
  // console.log(joke);
  val.push(joke);
  const root = document.querySelector(".root");

  val.forEach(function(c){
    console.log(c)
    a = ` 
    ${c}
   
  
      `;
  //parentNode.parentNode.remove()
    root.innerHTML += a;
  })


})();
