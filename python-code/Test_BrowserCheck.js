var UiObject = require("tools/UiObject");
var sleep = require("tools/sleep");
var UiSelector = require("tools/UiSelector");
var UiDevice = require("tools/UiDevice");

UiDevice.pressHome();
sleep(2000);

describe("Test case suites",function(){
	it("check browser app",function(){
    UiDevice.swipe(100,400,1000,400,10);//swipe to applist
    sleep(3000);
    var browserObj=new UiObject(new UiSelector().text("浏览器"));
    var dialogObj=new UiObject(new UiSelector().resourceId("ctaDialog.acceptButton"));
    var searchObj=new UiObject(new UiSelector().resourceId("search_hotword"));
    browserObj.click();
    sleep(3000);
    if (dialogObj.exists()) {
        dialogObj.click();
        sleep(3000);
    }
    expect(searchObj.exists()).toBe(true);
    
    UiDevice.pressBack();
    sleep(1000);
    UiDevice.pressBack();
  });
});