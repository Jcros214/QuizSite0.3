// function created before
function ExecPythonCommand(pythonCommand){
    var request = new XMLHttpRequest()
    request.open("GET", "/func/" + pythonCommand, true)
    request.send()
}


// function to print Hi!
function PrintHi(){
    ExecPythonCommand("print('Hi!')") 
}


// function to print hour
function PrintHour(){
    ExecPythonCommand("import datetime as dt<br>print(dt.datetime.now().hour)")
    // in python script you was need import datatime as dt or pass all in the
    // function, for example ExecPythonCommand("import datetime as dt<br>print(dt.datetime.now().hour)")
    // and use <br> to break line (in python script i'm was converting to normal \n, using \n here has not working)
}


// function to do anything
function FunctionName(){
    ExecPythonCommand("some command") 
}