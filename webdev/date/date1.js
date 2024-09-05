var d= new Date();
           document.getElementById("display").innerHTML = d;

/*Array */
              var month = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"];

console.log(d.getFullYear());
console.log(d.getMonth());
var m = d.getMonth();

document.getElementById("mnth").innerHTML = month[m];