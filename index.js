const axios = require('axios');

async function getUsers() {
  try {
    const response = await axios.get('https://jsonplaceholder.typicode.com/users');
    console.log(response.data);
  } catch (error) {
    console.error('Error fetching users:', error);
  }
}

getUsers();