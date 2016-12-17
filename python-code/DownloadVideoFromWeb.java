package com.yunos.mtbf.tests.browser;

import junit.framework.AssertionFailedError;

import com.yunos.mtbf.modules.browser.IMtbfBrowser;
import com.yunos.mtbf.tests.util.MtbfFactory;
import com.yunos.mtbf.tests.util.MtbfTestCase;
import com.yunos.test.uitest.modules.browser.IBrowser;
import com.yunos.test.uitest.modules.setting.ISetting;
import com.yunos.test.uitest.modules.util.Factory;
import com.yunos.test.uitest.modules.util.ViewException;

public class DownloadVideoFromWeb extends MtbfTestCase {

    IMtbfBrowser iMtbfBrowser;
    IBrowser iBrowser;
    ISetting iSetting;
    public static String URL = "http://main.gslb.ku6.com/s1/Lp5B29_kds41bG1P/1339446638643/f500e26a213313dff6bdd4753f86dfe4/1477051328810/v498/88/73/56ea5386fe5511ee6629fe589a3b8c11-f4v-h264-aac-299-32-120976.0-5198905-1339471125365-6d396fff5bc6c49c1caeb1d21231fc78-1-00-00-00.f4v?rate=299";

    @Override
    protected void setUp() throws Exception {
        super.setUp();
        iMtbfBrowser = MtbfFactory.getBrowserModule(iTestEngine);
        iBrowser = Factory.getBrowserModule(iTestEngine);
        iSetting = Factory.getSettingModule(iTestEngine);
    }

    @Override
    protected void prepareToRun() throws ViewException {
        super.prepareToRun();
        iHome.startSettingFromHomeScreen();
        iSetting.openAndConnectToWlan(iTestEngine.getConfigProperty("WLAN_ID"), iTestEngine.getConfigProperty("WLAN_PWD"), iTestEngine.getConfigProperty("WLAN_IDENTITY"));
        iTestEngine.sleep(2000);
        iTestEngine.pressBackNTimes(5);
        iHome.startBrowserFromHomeScreen();
        iBrowser.clearBrowserData();
    }

    public void runMtbf() throws ViewException {
        iBrowser.openLink(URL);
        iMtbfBrowser.downloadVideoFromWebLink(URL);
        iMtbfBrowser.openDownloadedVideoFileAndDelete();
        iTestEngine.sleep(2000);
        iTestEngine.pressBackNTimes(5);
        iHome.startBrowserFromHomeScreen();
    }

    @Override
    protected void tearDown() throws Exception {
        iBrowser.exitBrowser();
        super.tearDown();
    }

    protected void handleFail() {
        try {
            super.handleFail();
            iHome.startBrowserFromHomeScreen();
        } catch (Exception exception) {
            iTestEngine.log(TAG_NAME, "handleFail:" + exception);
        } catch (AssertionFailedError error) {
            iTestEngine.log(TAG_NAME, "handleFail:" + error);
        }
    }
}
