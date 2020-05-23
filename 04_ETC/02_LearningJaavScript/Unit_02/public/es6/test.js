'use strict'
const sentences = [
    { subject: 'JavaScript(P)', verb: 'is', object: 'great' },
    { subject: 'Elephants(P)', verb: 'are', object: 'large' }
];

function say({ subject, verb, object }) {
    console.log(`${subject} ${verb} ${object}`)
}

for (let s of sentences) {
    say(s)
}