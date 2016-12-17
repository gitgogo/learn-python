#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import re
import time
import logging
import unittest
import shutil
import inspect
from dependency.imagehelper import *
from dependency.parametrized_test_case import ParametrizedTestCase
from dependency.automation_device import AutomationDevice
from dependency.account import Account
from dependency import constants
from dependency.apk_manager import ApkManager
from muat_report import MuatReport, GenerateResult
from dependency.adb_log import AdbLog
from dependency.adb_mouse import AdbMouse
from dependency.adb_tools import AdbTools


# Init logger
logger_name = '%s-%s' % (constants.LOGGER_CLIENT_MUAT, os.getpid())
logger = logging.getLogger(logger_name)

class BrowserTest(ParametrizedTestCase):
    def setUp(self):
        # check monitor running status
        if self.mon and not self.mon.running_status:
            self.skipTest('process monitor stop')

        self.d      = AutomationDevice().get_device()
        self.account = Account(self.d)
        self.mouse = AdbMouse()
        self.adb_tools = AdbTools()
        
        self.BaseImagePath = os.path.join(os.path.abspath(os.path.dirname("__file__")), "dependency", "BaseImage")
        self.FailureIamgePath = os.path.join(os.path.abspath(os.path.dirname("__file__")), "test-reports", "FailureImage")
        self.TmpImagePath = os.path.join(os.path.abspath(os.path.dirname("__file__")), "test-reports", "TmpImage")
        
        if not os.path.exists(self.TmpImagePath):
            os.mkdir(self.TmpImagePath)
        if not os.path.exists(os.path.join(self.TmpImagePath, "croped")):
            os.mkdir(os.path.join(self.TmpImagePath, "croped"))

        self.account.sleep()
        self.account.wakeup()
        self.account.login()
        closeButton = self.d(resourceId="android:id/pc_close", className="android.widget.ImageView", packageName="com.android.browser")
        if closeButton.exists:
            logger.debug('click close button: (%s)' % (closeButton.info['packageName']))
            closeButton.click()
        self.adb_tools.adb_shell('am force-stop com.android.browser')     

    def tearDown(self):
        closeButton = self.d(resourceId="android:id/pc_close", className="android.widget.ImageView", packageName="com.android.browser")
        if closeButton.exists:
            logger.debug('click close button: (%s)' % (closeButton.info['packageName']))
            closeButton.click()
        self.adb_tools.adb_shell('am force-stop com.android.browser')    
        if os.path.exists(self.TmpImagePath):
            shutil.rmtree(self.TmpImagePath)
        self.account.sleep()
            
    def test_OpenAndExit(self):
        logger.info('Enter -- MUAT:BrowserTest:test_OpenAndExit')
        BrowserIcon = self.d(text=u"浏览器", className="android.widget.TextView")
        click_x = BrowserIcon.info['visibleBounds']['left'] +5
        click_y = BrowserIcon.info['visibleBounds']['top'] +5
        self.mouse.doubleclick(click_x, click_y, constants.MouseLeftKey)
        
        BrowserWindow = self.d(className="android.widget.FrameLayout", packageName="com.android.browser")
        self.assertTrue(BrowserWindow.exists)
        if BrowserWindow.exists:
            closeButton = self.d(resourceId="android:id/pc_close", className="android.widget.ImageView", packageName="com.android.browser")
            if closeButton.exists:
                logger.debug('click close button: (%s)' % (closeButton.info['packageName']))
                closeButton.click()
        logger.info('Exit -- MUAT:BrowserTest:test_OpenAndExit')
    
    def test_BlankPage(self):
        logger.info('Enter -- MUAT:BrowserTest:test_BlankPage')
        BrowserIcon = self.d(text=u"浏览器", className="android.widget.TextView")
        click_x = BrowserIcon.info['visibleBounds']['left'] +5
        click_y = BrowserIcon.info['visibleBounds']['top'] +5
        self.mouse.doubleclick(click_x, click_y, constants.MouseLeftKey)
        
        BrowserWindow = self.d(className="android.widget.FrameLayout", packageName="com.android.browser")
        self.assertTrue(BrowserWindow.exists)
        if BrowserWindow.exists:
            blankpage = self.d(resourceId="com.android.browser:id/title")
            if blankpage.exists:
                logger.info(blankpage.info)
                self.assertEqual(blankpage.info['text'], u'about:blank')
            address = self.d(resourceId="com.android.browser:id/url")
            if address.exists:
                self.assertEqual(address.info['text'], u"about:blank")
            
            closeButton = self.d(resourceId="android:id/pc_close", className="android.widget.ImageView", packageName="com.android.browser")
            if closeButton.exists:
                logger.debug('click close button: (%s)' % (closeButton.info['packageName']))
                closeButton.click()
        logger.info('Exit -- MUAT:BrowserTest:test_BlankPage')
    
    def test_InputAddr(self):
        logger.info('Enter -- MUAT:BrowserTest:test_InputAddr')
        BrowserIcon = self.d(text=u"浏览器", className="android.widget.TextView")
        click_x = BrowserIcon.info['visibleBounds']['left'] +5
        click_y = BrowserIcon.info['visibleBounds']['top'] +5
        self.mouse.doubleclick(click_x, click_y, constants.MouseLeftKey)
        
        BrowserWindow = self.d(className="android.widget.FrameLayout", packageName="com.android.browser")
        self.assertTrue(BrowserWindow.exists)
        if BrowserWindow.exists:
            blankpage = self.d(resourceId="com.android.browser:id/title")
            if blankpage.exists:
                self.assertEqual(blankpage.info['text'], "about:blank")
				#self.assertEqual(blankpage.info["text"],"about:blank")
            address = self.d(resourceId="com.android.browser:id/url")
            if address.exists:
                self.assertEqual(address.info['text'], "about:blank")
                address.clear_text()
                address.set_text("www.baidu.com")
                self.d.press(0x42)
                time.sleep(5)
                baiduPage = self.d(resourceId="com.android.browser:id/title")
                if baiduPage.exists:
                    self.assertEqual(baiduPage.info['text'], u'百度一下，你就知道')
                            
            closeButton = self.d(resourceId="android:id/pc_close", className="android.widget.ImageView", packageName="com.android.browser")
            if closeButton.exists:
                logger.debug('click close button: (%s)' % (closeButton.info['packageName']))
                closeButton.click()
        logger.info('Exit -- MUAT:BrowserTest:test_InputAddr')
    
    def test_RefreshPage(self):
        logger.info('Enter -- MUAT:BrowserTest:test_RefreshPage')
        BrowserIcon = self.d(text=u"浏览器", className="android.widget.TextView")
        click_x = BrowserIcon.info['visibleBounds']['left'] +5
        click_y = BrowserIcon.info['visibleBounds']['top'] +5
        self.mouse.doubleclick(click_x, click_y, constants.MouseLeftKey)
        
        BrowserWindow = self.d(className="android.widget.FrameLayout", packageName="com.android.browser")
        self.assertTrue(BrowserWindow.exists)
        if BrowserWindow.exists:
            self.assertTrue(self.d.press(0x8d))
            time.sleep(2)
            blankpage = self.d(resourceId="com.android.browser:id/title")
            if blankpage.exists:
                self.assertEqual(blankpage.info['text'], "about:blank")
            address = self.d(resourceId="com.android.browser:id/url")
            if address.exists:
                self.assertEqual(address.info['text'], "about:blank")
                address.clear_text()
                address.set_text("time")
                self.d.press(0x42)
                time.sleep(15)
                timebaiduPage = self.d(resourceId="com.android.browser:id/title")
                if timebaiduPage.exists:
                    if timebaiduPage.info['text'] == u'time_百度搜索':
                        name1 = "test_RefreshPage_%s.jpg" % time.strftime('%Y%m%d%H%M%S', time.localtime())
                        img = os.path.join(self.TmpImagePath, name1)
                        self.d.screenshot(img)
                        cropedImgPath1 = os.path.join(self.TmpImagePath, "croped", name1.replace(".jpg", "_croped.jpg"))
                        CropImage(img, cropedImgPath1, 125, 266, 470, 366)

                        refreshButton = self.d(resourceId="com.android.browser:id/stop", className="android.widget.ImageButton", packageName="com.android.browser")
                        if refreshButton.exists:
                            refreshButton.click()
                            time.sleep(15)
                        
                            name2 = "test_RefreshPage_%s.jpg" % time.strftime('%Y%m%d%H%M%S', time.localtime())
                            img = os.path.join(self.TmpImagePath, name2)
                            self.d.screenshot(img)
                            cropedImgPath2 = os.path.join(self.TmpImagePath, "croped", name2.replace(".jpg", "_croped.jpg"))
                            CropImage(img, cropedImgPath2, 125, 266, 470, 366)
                            
                            if  CompareImage(cropedImgPath1, cropedImgPath2, 0.99):
                                shutil.copy(cropedImgPath1, os.path.join(self.FailureIamgePath, name1.replace(".jpg", "_failure.jpg")))
                                shutil.copy(cropedImgPath2, os.path.join(self.FailureIamgePath, name2.replace(".jpg", "_failure.jpg")))
                                path = os.path.join(self.FailureIamgePath, name1.replace(".jpg", "_failure.jpg"))
                                self.fail("The failure file path is %s" % path)
            pageCloseBt = self.d(resourceId="com.android.browser:id/close")
            if pageCloseBt.exists:
                pageCloseBt.click()
            closeButton = self.d(resourceId="android:id/pc_close", className="android.widget.ImageView", packageName="com.android.browser")
            if closeButton.exists:
                logger.debug('click close button: (%s)' % (closeButton.info['packageName']))
                closeButton.click()
        logger.info('Exit -- MUAT:BrowserTest:test_RefreshPage')
        
    def test_ForwardOrBackwrad(self):
        logger.info('Enter -- MUAT:BrowserTest:test_ForwardOrBackwrad')
        BrowserIcon = self.d(text=u"浏览器", className="android.widget.TextView")
        click_x = BrowserIcon.info['visibleBounds']['left'] +5
        click_y = BrowserIcon.info['visibleBounds']['top'] +5
        self.mouse.doubleclick(click_x, click_y, constants.MouseLeftKey)
        
        BrowserWindow = self.d(className="android.widget.FrameLayout", packageName="com.android.browser")
        self.assertTrue(BrowserWindow.exists)
        if BrowserWindow.exists:
            blankpage = self.d(resourceId="com.android.browser:id/title")
            if blankpage.exists:
                self.assertEqual(blankpage.info['text'], "about:blank")
            address = self.d(resourceId="com.android.browser:id/url")
            if address.exists:
                self.assertEqual(address.info['text'], "about:blank")
                address.clear_text()
                address.set_text("www.baidu.com")
                self.d.press(0x42)
                time.sleep(5)
                baiduPage = self.d(resourceId="com.android.browser:id/title")
                if baiduPage.exists:
                    if baiduPage.info['text'] == u'百度一下，你就知道':
                        address = self.d(resourceId="com.android.browser:id/url")
                        if address.exists:
                            address.clear_text()
                            address.set_text("www.taobao.com")
                            self.d.press(0x42)
                            time.sleep(5)
                            
                            taobaoPage = self.d(resourceId="com.android.browser:id/title")
                            if taobaoPage.exists:
                                self.assertEqual(taobaoPage.info['text'], u'淘宝网 - 淘！我喜欢')
                                backButton = self.d(resourceId="com.android.browser:id/back", className="android.widget.ImageButton", packageName="com.android.browser")
                                if backButton.exists:
                                    backButton.click()
                                    time.sleep(5)
                                    baiduPage = self.d(resourceId="com.android.browser:id/title")
                                    if baiduPage.exists:
                                        self.assertEqual(baiduPage.info['text'], u'百度一下，你就知道')
                                    forwardButton = self.d(resourceId="com.android.browser:id/forward", className="android.widget.ImageButton", packageName="com.android.browser")
                                    if forwardButton.exists:
                                        forwardButton.click()
                                        time.sleep(5)
                                        taobaoPage = self.d(resourceId="com.android.browser:id/title")
                                        if taobaoPage.exists:
                                            self.assertEqual(taobaoPage.info['text'], u'淘宝网 - 淘！我喜欢')
                                            
            closeButton = self.d(resourceId="android:id/pc_close", className="android.widget.ImageView", packageName="com.android.browser")
            if closeButton.exists:
                logger.debug('click close button: (%s)' % (closeButton.info['packageName']))
                closeButton.click()
        logger.info('Exit -- MUAT:BrowserTest:test_ForwardOrBackwrad')
        
    
    def test_BaiduSearch(self):
        logger.info('Enter -- MUAT:BrowserTest:test_BaiduSearch')
        BrowserIcon = self.d(text=u"浏览器", className="android.widget.TextView")
        click_x = BrowserIcon.info['visibleBounds']['left'] +5
        click_y = BrowserIcon.info['visibleBounds']['top'] +5
        self.mouse.doubleclick(click_x, click_y, constants.MouseLeftKey)
        time.sleep(3)
        BrowserWindow = self.d(className="android.widget.FrameLayout", packageName="com.android.browser")
        self.assertTrue(BrowserWindow.exists)
        if BrowserWindow.exists:
            blankpage = self.d(resourceId="com.android.browser:id/title")
            if blankpage.exists:
                self.assertEqual(blankpage.info['text'], "about:blank")
            address = self.d(resourceId="com.android.browser:id/url")
            if address.exists:
                self.assertEqual(address.info['text'], "about:blank")
                address.clear_text()
                address.set_text("time")
                self.d.press(0x42)
                time.sleep(15)
                timebaiduPage = self.d(resourceId="com.android.browser:id/title")
                if timebaiduPage.exists:
                    self.assertEqual(timebaiduPage.info['text'], u'time_百度搜索')
                    
            pageCloseBt = self.d(resourceId="com.android.browser:id/close")
            if pageCloseBt.exists:
                pageCloseBt.click()       
            closeButton = self.d(resourceId="android:id/pc_close", className="android.widget.ImageView", packageName="com.android.browser")
            if closeButton.exists:
                logger.debug('click close button: (%s)' % (closeButton.info['packageName']))
                closeButton.click()
        logger.info('Exit -- MUAT:BrowserTest:test_BaiduSearch')
    
    def test_EmptyBookmark(self):
        logger.info('Enter -- MUAT:BrowserTest:test_EmptyBookmark')
        BrowserIcon = self.d(text=u"浏览器", className="android.widget.TextView")
        click_x = BrowserIcon.info['visibleBounds']['left'] +5
        click_y = BrowserIcon.info['visibleBounds']['top'] +5
        self.mouse.doubleclick(click_x, click_y, constants.MouseLeftKey)
        
        BrowserWindow = self.d(className="android.widget.FrameLayout", packageName="com.android.browser")
        self.assertTrue(BrowserWindow.exists)
        if BrowserWindow.exists:
            bookmarkButton = self.d(resourceId="com.android.browser:id/star", className="android.widget.ImageButton", packageName="com.android.browser")
            if bookmarkButton.exists:
                bookmarkButton.click()
                time.sleep(2)
                bookmarkLabel = self.d(resourceId="com.android.browser:id/label")
                self.assertFalse(bookmarkLabel.exists)
                
            closeButton = self.d(resourceId="android:id/pc_close", className="android.widget.ImageView", packageName="com.android.browser")
            if closeButton.exists:
                logger.debug('click close button: (%s)' % (closeButton.info['packageName']))
                closeButton.click()
        logger.info('Exit -- MUAT:BrowserTest:test_EmptyBookmark')
        
    def test_SearchWebPage(self):
        logger.info('Enter -- MUAT:BrowserTest:test_SearchWebPage')
        BrowserIcon = self.d(text=u"浏览器", className="android.widget.TextView")
        click_x = BrowserIcon.info['visibleBounds']['left'] +5
        click_y = BrowserIcon.info['visibleBounds']['top'] +5
        self.mouse.doubleclick(click_x, click_y, constants.MouseLeftKey)
        BrowserWindow = self.d(className="android.widget.FrameLayout", packageName="com.android.browser")
        self.assertTrue(BrowserWindow.exists)
        if BrowserWindow.exists:
            self.assertTrue(self.d.press(0x8d))
            blankpage = self.d(resourceId="com.android.browser:id/title")
            if blankpage.exists:
                self.assertEqual(blankpage.info['text'], u"about:blank")
            address = self.d(resourceId="com.android.browser:id/url")
            if address.exists:
                self.assertEqual(address.info['text'], "about:blank")
                address.clear_text()
                address.set_text("www.baidu.com")
                self.d.press(0x42)
                time.sleep(5)
                baiduPage = self.d(resourceId="com.android.browser:id/title")
                if baiduPage.exists:
                    self.assertEqual(baiduPage.info['text'], u'百度一下，你就知道')
                    for button in self.d(className="android.widget.ImageButton", packageName="com.android.browser"):
                        if button.info['contentDescription'] == u'更多选项':
                            button.click()
                            searchButton = self.d(text=u"在网页上查找", resourceId="android:id/title")
                            if searchButton.exists:
                                searchButton.click()
                                editView = self.d(text=u"在网页上查找", resourceId="android:id/edit")
                                if editView.exists:
                                    editView.clear_text()
                                    editView.set_text(u"About")
                                    time.sleep(3)
                                    BaseImg = os.path.join(self.BaseImagePath, "test_SearchWebPage.jpg")
                                    name = "test_SearchWebPage_%s.jpg" % time.strftime('%Y%m%d%H%M%S', time.localtime())
                                    img = os.path.join(self.TmpImagePath, name)
                                    self.d.screenshot(img)
                                    cropedImgPath = os.path.join(self.TmpImagePath, "croped", name.replace(".jpg", "_croped.jpg"))
                                    CropImage(img, cropedImgPath, 1000, 945, 1090, 970)
                                    if not CompareImage(cropedImgPath, BaseImg, 0.99):
                                        shutil.copy(cropedImgPath, os.path.join(self.FailureIamgePath, name.replace(".jpg", "_failure.jpg")))
                                        path = os.path.join(self.FailureIamgePath, name.replace(".jpg", "_failure.jpg"))
                                        self.fail("The failure file path is %s" % path)
                            break
                                    
            closeButton = self.d(resourceId="android:id/pc_close", className="android.widget.ImageView", packageName="com.android.browser")
            if closeButton.exists:
                logger.debug('click close button: (%s)' % (closeButton.info['packageName']))
                closeButton.click()
        logger.info('Exit -- MUAT:BrowserTest:test_SearchWebPage')
