function fname() {
    // window.alert("hey hey");
    var name = document.getElementById("name").value;
    // window.alert(name);
    var pname = /^[A-Za-z ]{3,15}$/;
    if (!pname.test(name)) {
        //window.alert(name);
        document.getElementById("name").style.border = "3px solid red";


    }
    else {
        document.getElementById("name").style.border = "3px solid green";
    }
}
function contact() {
    //window.alert("hey hey");
    var number = document.getElementById("number").value;
    // window.alert(number);
    var pnumber = /^[0-9]{10}$/;
    if (!pnumber.test(number)) {
        //  window.alert(number);
        document.getElementById("number").style.border = "3px solid red";
    }
    else {
        document.getElementById("number").style.border = "3px solid green";
    }
}
function mail() {
    // window.alert("hey hey");
    var email = document.getElementById("email").value;
    //window.alert(email);
    var pemail = /^[a-z0-9./+]+@[a-z0-9./+]+\.[a-z]{3,8}$/;
    if (!pemail.test(email)) {
        //  window.alert(email);
        document.getElementById("email").style.border = "3px solid red";
    }
    else {
        document.getElementById("email").style.border = "3px solid green";
    }
}
