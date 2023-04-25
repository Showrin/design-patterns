class SettingsManager {
  static instance = undefined;

  constructor() {
    if (SettingsManager.instance === undefined) {
      SettingsManager.instance = this;
    }

    return SettingsManager.instance;
  }
}

const a = new SettingsManager();
a.color = "red";

const b = new SettingsManager();
b.color = "blue";

// a & b will display the same instance object
console.log(a.color);
console.log(b.color);
console.log(a === b);

// Output
// blue
// blue
// true
