import _ from 'lodash';
import { cube } from './math.js';

function component() {
  let element = document.createElement('pre');

  element.innerHTML = [
    'Hello webpack',
    cube(5)
  ].join('\n\n');
  
  return element;
}

document.body.appendChild(component());

if (process.env.NODE_ENV == 'production') {
  console.log('Look!your mother fucker!');
}