// Greeter.js
// 模块组件
import React, {Component} from 'react'
import config from './config.json';
import styles from './Greeter.css'; // CSS模块化，样式表只作用在当前组件

class Greeter extends Component{
  render() {
    return (
      <div className={styles.root}>
        {config.greetText}
        <p className={styles.child}>Greeting!!!</p>
      </div>
    );
  }
}

export default Greeter