function resolveAfter2Seconds() {
  return new Promise(resolve => {
    setTimeout(() => {
      console.log("Calling resolved")
      // resolve('remeoutsolved');
    }, 2000);
  });
}

async function asyncCall() {
  console.log('calling');
  const result = resolveAfter2Seconds();
  console.log("Async Print");
  // expected output: 'resolved'
}

asyncCall();