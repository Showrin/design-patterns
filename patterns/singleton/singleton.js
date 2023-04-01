class SettingsManager {
  static instance = undefined

  constructor(settings) {
    if (SettingsManager.instance === undefined) {
      SettingsManager.instance = settings;
    }
  }

  getSettings() {
    return SettingsManager.instance
  }

  set(key, value) {
    SettingsManager.instance[key] = value
  }
}

const a = new SettingsManager({})
a.set("name", "Showrin");

const b = new SettingsManager({});
b.set("id", "1234");

console.log(a.getSettings(),b.getSettings(), SettingsManager.instance) //  a & b will display the same instance dictionary
