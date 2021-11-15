
let MyFt_list = document.getElementById('ft_list');

function eraseCookie(name) {   
    document.cookie = name + '=; Max-Age=-99999999;';  
}

function deleteMe(a){ 
    if(window.confirm("Wanna delete da line ?")) {
        eraseCookie(a.textContent)
        a.remove();
    }
}
// si annuler alors renvoie : null

function createBulletPoint(BulletP) {
    //Cree la nouvelle div
    let newDiv = document.createElement('div');
    MyFt_list.insertBefore(newDiv, MyFt_list.firstChild);

    //Cree le bullet point en child sous la div
    let newLi = document.createElement('li');
    newLi.textContent = BulletP;
    newLi.setAttribute('onclick', "deleteMe(this)");
    newDiv.insertBefore(newLi, newDiv.firstChild);

}    

function askBulletPoint(){ 
    let todoTxt =  window.prompt("Que devez-vous faire ?")
    if (todoTxt !== "" && todoTxt !== null) {
        createBulletPoint(todoTxt)
        //Push un cookie
        document.cookie = todoTxt + '=; Max-Age=9999;';
        let MyCookie = document.cookie;
        console.log(MyCookie);
    }
    


}

function recreateTodo(){
    
    if(document.cookie != ""){
        let decodedCookie = decodeURIComponent(document.cookie);
        let ca = decodedCookie.split(';');
        let car = ca.reverse()
        for (const element of car){
            createBulletPoint(element.substring(0, element.length-1));
        }
    }    

}

