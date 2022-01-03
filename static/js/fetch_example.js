console.log('inside fetch js file');


function myFunction() {
    console.log('clicked');
    fetch('https://reqres.in/api/users?page=2').then(
        response => response.json()
    ).then(
        response_obj => put_users_inside_html(response_obj.data)
    ).catch(
        error => console.log(error)
    )
}

function put_users_inside_html(response_obj) {
    const curr_main = document.querySelector("main");
    for (let user of response_obj){
        const section = document.createElement('section');
        section.innerHTML = `
        <img src="${user.avatar}" alt="Profile Picture"/>
        <div>
            <span>${user.first_name} ${user.last_name}</span>
            <br>
            <a href="mailto:${user.email}">Send Email</a>
        </div>
        `;
        curr_main.appendChild(section);
    }

}

// function createUsersList(users){
//     console.log(users);
//     const user = users[0];
//     console.log(user);
//     const curr_main = document.querySelector("main");
//     for(let user of users){
//         const section = document.createElement('section');
//         section.innerHTML = `
//         <img src="${user.avatar}" alt="Profile Picture"/>
//         <div>
//             <span>${user.first_name} ${user.last_name}</span>
//             <br>
//             <a href="mailto:${user.email}">Send Email</a>
//         </div>
//         `;
//         curr_main.appendChild(section);
//     }
// }