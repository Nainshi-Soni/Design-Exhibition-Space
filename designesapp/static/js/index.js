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
function pas() {
    //  window.alert("ram ram");
    var pass = document.getElementById("pass").value;
    //window.alert(pass);
    //pattern for strong password
    var pps = /^[A-Za-z]+[A-Za-z0-9.@$#*/%&*^_(+\[+\]+{\+\})+!]+[A-Za-z0-9@$*.#%&*^_(+\[+\]+{\+\})+!]+[A-Za-z0-9.@$*/#%&*^_(+\[+\]+{\+\})+!]{5,}$/;
    var ppass = /^[A-Za-z]{1,}$/;
    //pattern for weak password
    var ppas = /^[A-Za-z0-9]+[A-Za-z0-9]{3,}$/;
    ////pattern for medium password
    if (ppass.test(pass)) {
        //window.alert(pps);
       // document.getElementById("sp2").innerHTML = "weak password";
       // document.getElementById("sp2").style.color = "red";
        document.getElementById("pass").style.border = "3px solid red";
       // document.getElementById("hw").innerHTML = "if you enter alphabet and number between 0-9 than you create the medium password";
    }
    else if (ppas.test(pass)) {
       // document.getElementById("sp2").innerHTML = "medium password";
       // document.getElementById("sp2").style.color = "yellow";
        document.getElementById("pass").style.border = "3px solid yellow";
       // document.getElementById("hw").innerHTML = "if you want to create strong password then please enter some alphabet and minimum 1special character and  minimum one number between 0-9 than the pass is strong pass";
    }
    else if (pps.test(pass)) {
       // document.getElementById("sp2").innerHTML = "strong password";
       // document.getElementById("sp2").style.color = "green";
        document.getElementById("pass").style.border = "3px solid green";
     //   document.getElementById("hw").innerHTML = "you created the strong password ";
    }
    else {
        pas();
    }


}