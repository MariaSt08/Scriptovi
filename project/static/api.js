const BASE_URL = 'http://localhost:5000/api';
console.log("loaded api")
async function createUser(username, password) {
    const url = `${BASE_URL}/users`;
    const payload = {
        username: username,
        password: password
    };

    const response = await fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(payload)
    });

    const data = await response.json();
    return data;
}

async function getUsers() {
    const url = `${BASE_URL}/users`;
    const response = await fetch(url, {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json'
        }
    });

    const data = await response.json();
    return data;
}

async function login(username,password) {
    const url = `${BASE_URL}/login`;
    
    const response = await fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            "username":username,
            "password":password
        })
    });

    

    const data = await response.json();
    return data;
}

// Function to create a todo
async function createTodo(title, description, userId) {
    const url = `${BASE_URL}/todos`;
    const payload = {
        title: title,
        description: description,
        user_id: userId
    };

    const response = await fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(payload)
    });

    const data = await response.json();
    return data;
}

async function getTodos(userId) {
    const url = `${BASE_URL}/todos/${userId}`;

    const response = await fetch(url, {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json'
        }
    });

    const data = await response.json();
    return data;
}

async function getTodo(todoId) {
    const url = `${BASE_URL}/todos/${todoId}`;
    const response = await fetch(url, {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json'
        }
    });

    const data = await response.json();
    return data;
}

// Function to update a todo
async function updateTodo(todoId, title, description, done) {
    const url = `${BASE_URL}/todos/${todoId}`;
    const payload = {
        title: title,
        description: description,
        done: done
    };

    const response = await fetch(url, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(payload)
    });

    const data = await response.json();
    return data;
}

// Function to delete a todo
async function deleteTodo(todoId) {
    const url = `${BASE_URL}/todos/${todoId}`;
    const response = await fetch(url, {
        method: 'DELETE',
        headers: {
            'Content-Type': 'application/json'
        }
    });

    return response.status;
}

// Export the functions for use in other files
export {
    createUser,
    getUsers,
    login,
    createTodo,
    getTodos,
    getTodo,
    updateTodo,
    deleteTodo
};
