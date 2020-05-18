function studMain(){
    var mainIndex = document.getElementById("mainIndex").style.display = "none";
    var studBlock = document.getElementById("studBlock").style.display = "block"; 
    var navBar1 = document.getElementById("nav_home").style.display = "block";
    var studProfForm = document.getElementById("StudProfForm").style.display = "none";
}

function addStudForm(){
    var studBlock = document.getElementById("studBlock").style.display = "none"; 
    var studForm = document.getElementById("AddStudForm").style.display = "block";
    var navBar1 = document.getElementById("nav_home").style.display = "block";
    var navBar2 = document.getElementById("nav_back").style.display = "block";
    var studProfForm = document.getElementById("StudProfForm").style.display = "none";
}

function showOnStudMain(){
    var studBlock = document.getElementById("studBlock").style.display = "block";
    var studForm = document.getElementById("AddStudForm").style.display = "none";
    var navBar2 = document.getElementById("nav_back").style.display = "none";
    var studProfForm = document.getElementById("StudProfForm").style.display = "none";
}

function StudProfForm(){
    var studBlock = document.getElementById("studBlock").style.display = "none";
    var studProfForm = document.getElementById("StudProfForm").style.display = "block";
    var navBar1 = document.getElementById("nav_home").style.display = "block";
    var navBar2 = document.getElementById("nav_back").style.display = "block";
}