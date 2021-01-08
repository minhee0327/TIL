const myLogger = (store) => (next) => (action) => {
  //   console.log(action);
  //   const result = next(action);
  //   console.log("\t", store.getState());

  typeof actioni === "function"
    ? action(store.dispatch, store.getState)
    : next(action);

  //   return result;
};

export default myLogger;
