import datetime
import re
import time
import json
from functools import reduce
from logzero import logger
import tidevice
import solox.public._iosPerf as iosP
from solox.public.iosperf._perf import DataType, Performance
from solox.public.adb import adb
from solox.public.common import Devices, file
from solox.public.fps import FPSMonitor, TimeUtils

d = Devices()
f = file()


class CPU:

    def __init__(self, pkgName, deviceId, platform='Android'):
        self.pkgName = pkgName
        self.deviceId = deviceId
        self.platform = platform
        self.apm_time = datetime.datetime.now().strftime('%H:%M:%S.%f')

    def getprocessCpuStat(self):
        """get the cpu usage of a process at a certain time"""
        pid = d.getPid(pkgName=self.pkgName, deviceId=self.deviceId)
        cmd = f'cat /proc/{pid}/stat'
        result = adb.shell(cmd=cmd, deviceId=self.deviceId)
        r = re.compile("\\s+")
        toks = r.split(result)
        processCpu = float(int(toks[13]) + int(toks[14]) + int(toks[15]) + int(toks[16]))
        return processCpu

    def getTotalCpuStat(self):
        """get the total cpu usage at a certain time"""
        cmd = f'cat /proc/stat |{d._filterType()} ^cpu'
        result = adb.shell(cmd=cmd, deviceId=self.deviceId)
        r = re.compile(r'(?<!cpu)\d+')
        toks = r.findall(result)
        totalCpu = 0
        for i in range(1, 9):
            totalCpu += float(toks[i])
        return float(totalCpu)

    def getCpuCores(self):
        """get Android cpu cores"""
        cmd = f'cat /sys/devices/system/cpu/online'
        result = adb.shell(cmd=cmd, deviceId=self.deviceId)
        try:
            nums = int(result.split('-')[1]) + 1
        except:
            nums = 1
        return nums

    def getSysCpuStat(self):
        """get the total cpu usage at a certain time"""
        cmd = f'cat /proc/stat |{d._filterType()} ^cpu'
        result = adb.shell(cmd=cmd, deviceId=self.deviceId)
        r = re.compile(r'(?<!cpu)\d+')
        toks = r.findall(result)
        ileCpu = int(toks[4])
        sysCpu = self.getTotalCpuStat() - ileCpu
        return sysCpu

    def getAndroidCpuRate(self):
        """get the Android cpu rate of a process"""
        processCpuTime_1 = self.getprocessCpuStat()
        totalCpuTime_1 = self.getTotalCpuStat()
        sysCpuTime_1 = self.getSysCpuStat()
        time.sleep(1)
        processCpuTime_2 = self.getprocessCpuStat()
        totalCpuTime_2 = self.getTotalCpuStat()
        sysCpuTime_2 = self.getSysCpuStat()
        # syscpu usage=[( +sys_end+nice_end) - (user_begin + sys_begin+nice_begin)]/(total_end - total_begin)*100
        # appcpu usage=((utime + stime) - (utime_pre + stime_pre)) / (cpu_total - cpu_total_pre)
        appCpuRate = round(float((processCpuTime_2 - processCpuTime_1) / (totalCpuTime_2 - totalCpuTime_1) * 100), 2)
        sysCpuRate = round(float((sysCpuTime_2 - sysCpuTime_1) / (totalCpuTime_2 - totalCpuTime_1) * 100), 2)
        apm_time = datetime.datetime.now().strftime('%H:%M:%S')
        f.add_log(f'{f.report_dir}/cpu_app.log', apm_time, appCpuRate)
        f.add_log(f'{f.report_dir}/cpu_sys.log', apm_time, sysCpuRate)

        return appCpuRate, sysCpuRate

    def getiOSCpuRate(self):
        """get the iOS cpu rate of a process, unit:%"""
        apm = iosAPM(self.pkgName)
        appCpuRate = round(float(apm.getPerformance(apm.cpu)[0]), 2)
        sysCpuRate = round(float(apm.getPerformance(apm.cpu)[1]), 2)
        apm_time = datetime.datetime.now().strftime('%H:%M:%S')
        f.add_log(f'{f.report_dir}/cpu_app.log', apm_time, appCpuRate)
        f.add_log(f'{f.report_dir}/cpu_sys.log', apm_time, sysCpuRate)
        return appCpuRate, sysCpuRate

    def getCpuRate(self):
        """Get the cpu rate of a process, unit:%"""
        if self.platform == 'Android':
            appCpuRate, systemCpuRate = self.getAndroidCpuRate()
        else:
            appCpuRate, systemCpuRate = self.getiOSCpuRate()
        return appCpuRate, systemCpuRate


class MEM:
    def __init__(self, pkgName, deviceId, platform='Android'):
        self.pkgName = pkgName
        self.deviceId = deviceId
        self.platform = platform
        self.apm_time = datetime.datetime.now().strftime('%H:%M:%S')

    def getAndroidMem(self):
        """Get the Android memory ,unit:MB"""
        pid = d.getPid(pkgName=self.pkgName, deviceId=self.deviceId)
        cmd = f'dumpsys meminfo {pid}'
        output = adb.shell(cmd=cmd, deviceId=self.deviceId)
        m_total = re.search(r'TOTAL\s*(\d+)', output)
        m_native = re.search(r'Native Heap\s*(\d+)', output)
        m_dalvik = re.search(r'Dalvik Heap\s*(\d+)', output)
        totalPass = round(float(float(m_total.group(1))) / 1024, 2)
        nativePass = round(float(float(m_native.group(1))) / 1024, 2)
        dalvikPass = round(float(float(m_dalvik.group(1))) / 1024, 2)
        return totalPass, nativePass, dalvikPass

    def getiOSMem(self):
        """Get the iOS memory"""
        apm = iosAPM(self.pkgName)
        totalPass = round(float(apm.getPerformance(apm.memory)), 2)
        nativePass = 0
        dalvikPass = 0
        return totalPass, nativePass, dalvikPass

    def getProcessMem(self):
        """Get the app memory"""
        if self.platform == 'Android':
            totalPass, nativePass, dalvikPass = self.getAndroidMem()
        else:
            totalPass, nativePass, dalvikPass = self.getiOSMem()
        apm_time = datetime.datetime.now().strftime('%H:%M:%S')
        time.sleep(1)
        f.add_log(f'{f.report_dir}/mem_total.log', apm_time, totalPass)

        if self.platform == 'Android':
            f.add_log(f'{f.report_dir}/mem_native.log', apm_time, nativePass)
            f.add_log(f'{f.report_dir}/mem_dalvik.log', apm_time, dalvikPass)

        return totalPass, nativePass, dalvikPass


class Battery:
    def __init__(self, deviceId, platform='Android'):
        self.deviceId = deviceId
        self.platform = platform
        self.apm_time = datetime.datetime.now().strftime('%H:%M:%S')
    
    def getBattery(self):
        if self.platform == 'Android':
            level, temperature = self.getAndroidBattery()
            return level, temperature
        else:
            temperature, current, voltage, power = self.getiOSBattery()
            return temperature, current, voltage, power
        
    def getAndroidBattery(self):
        """Get android battery info, unit:%"""
        # Switch mobile phone battery to non-charging state
        cmd = 'dumpsys battery set status 1'
        adb.shell(cmd=cmd, deviceId=self.deviceId)
        # Get phone battery info
        cmd = 'dumpsys battery'
        output = adb.shell(cmd=cmd, deviceId=self.deviceId)
        level = int(re.findall(u'level:\s?(\d+)', output)[0])
        temperature = int(re.findall(u'temperature:\s?(\d+)', output)[0]) / 10
        time.sleep(1)
        apm_time = datetime.datetime.now().strftime('%H:%M:%S')
        f.add_log(f'{f.report_dir}/battery_level.log', apm_time, level)
        f.add_log(f'{f.report_dir}/battery_tem.log', apm_time, temperature)
        return level, temperature
    
    def getiOSBattery(self):
        """Get ios battery info, unit:%"""
        d  = tidevice.Device()
        ioDict =  d.get_io_power()
        tem = ioDict['Diagnostics']['IORegistry']['Temperature']
        current = abs(ioDict['Diagnostics']['IORegistry']['InstantAmperage'])
        voltage = ioDict['Diagnostics']['IORegistry']['Voltage']
        power = current * voltage / 1000
        apm_time = datetime.datetime.now().strftime('%H:%M:%S')
        f.add_log(f'{f.report_dir}/battery_tem.log', apm_time, tem) # unknown
        f.add_log(f'{f.report_dir}/battery_current.log', apm_time, current) #mA
        f.add_log(f'{f.report_dir}/battery_voltage.log', apm_time, voltage) #mV
        f.add_log(f'{f.report_dir}/battery_power.log', apm_time, power)
        return tem, current, voltage, power

    def recoverBattery(self):
        """Reset phone charging status"""
        cmd = 'dumpsys battery reset'
        adb.shell(cmd=cmd, deviceId=self.deviceId)


class Flow:

    def __init__(self, pkgName, deviceId, platform='Android'):
        self.pkgName = pkgName
        self.deviceId = deviceId
        self.platform = platform
        self.apm_time = datetime.datetime.now().strftime('%H:%M:%S')

    def getAndroidNet(self):
        """Get Android upflow and downflow data, unit:KB"""
        pid = d.getPid(pkgName=self.pkgName, deviceId=self.deviceId)
        cmd = f'cat /proc/{pid}/net/dev |{d._filterType()} wlan0'
        output_pre = adb.shell(cmd=cmd, deviceId=self.deviceId)
        m_pre = re.search(r'wlan0:\s*(\d+)\s*\d+\s*\d+\s*\d+\s*\d+\s*\d+\s*\d+\s*\d+\s*(\d+)', output_pre)
        sendNum_pre = round(float(float(m_pre.group(2)) / 1024), 2)
        recNum_pre = round(float(float(m_pre.group(1)) / 1024), 2)
        time.sleep(1)
        output_final = adb.shell(cmd=cmd, deviceId=self.deviceId)
        m_final = re.search(r'wlan0:\s*(\d+)\s*\d+\s*\d+\s*\d+\s*\d+\s*\d+\s*\d+\s*\d+\s*(\d+)', output_final)
        sendNum_final = round(float(float(m_final.group(2)) / 1024), 2)
        recNum_final = round(float(float(m_final.group(1)) / 1024), 2)
        sendNum = round(float(sendNum_final - sendNum_pre), 2)
        recNum = round(float(recNum_final - recNum_pre), 2)
        return sendNum, recNum
    

    def getiOSNet(self):
        """Get iOS upflow and downflow data"""
        apm = iosAPM(self.pkgName)
        apm_data = apm.getPerformance(apm.network)
        sendNum = round(float(apm_data[1]), 2)
        recNum = round(float(apm_data[0]), 2)
        return sendNum, recNum

    def getNetWorkData(self):
        """Get the upflow and downflow data, unit:KB"""
        if self.platform == 'Android':
            sendNum, recNum = self.getAndroidNet()
        else:
            sendNum, recNum = self.getiOSNet()
        apm_time = datetime.datetime.now().strftime('%H:%M:%S')
        f.add_log(f'{f.report_dir}/upflow.log', apm_time, sendNum)
        f.add_log(f'{f.report_dir}/downflow.log', apm_time, recNum)
        return sendNum, recNum


class FPS:

    def __init__(self, pkgName, deviceId, platform='Android', surfaceview='true'):
        self.pkgName = pkgName
        self.deviceId = deviceId
        self.platform = platform
        self.surfaceview = surfaceview
        self.apm_time = datetime.datetime.now().strftime('%H:%M:%S.%f')

    def getAndroidFps(self):
        """get Android Fps, unit:HZ"""
        monitors = FPSMonitor(device_id=self.deviceId, package_name=self.pkgName, frequency=1,
                              surfaceview=self.surfaceview, start_time=TimeUtils.getCurrentTimeUnderline())
        monitors.start()
        fps, jank = monitors.stop()
        apm_time = datetime.datetime.now().strftime('%H:%M:%S')
        f.add_log(f'{f.report_dir}/fps.log', apm_time, fps)
        f.add_log(f'{f.report_dir}/jank.log', apm_time, jank)
        return fps, jank

    def getiOSFps(self):
        """get iOS Fps"""
        apm = iosAPM(self.pkgName)
        fps = int(apm.getPerformance(apm.fps))
        apm_time = datetime.datetime.now().strftime('%H:%M:%S')
        f.add_log(f'{f.report_dir}/fps.log', apm_time, fps)
        return fps, 0

    def getFPS(self):
        """get fps、jank"""
        if self.platform == 'Android':
            fps, jank = self.getAndroidFps()
        else:
            fps, jank = self.getiOSFps()
        return fps, jank


class iosAPM():

    def __init__(self, pkgName, deviceId=tidevice.Device()):
        self.pkgName = pkgName
        self.deviceId = deviceId
        self.apm_time = datetime.datetime.now().strftime('%H:%M:%S.%f')
        self.cpu = DataType.CPU
        self.memory = DataType.MEMORY
        self.network = DataType.NETWORK
        self.fps = DataType.FPS
        self.perfs = 0
        self.app_cpu = 0
        self.sys_cpu = 0
        self.downflow = 0
        self.upflow = 0

    def callback(self, _type: DataType, value: dict):
        if _type == 'network':
            self.downflow = value['downFlow']
            self.upflow = value['upFlow']
        else:
            self.perfs = value['value']

    def getPerformance(self, perfTpe: DataType):
        if perfTpe == DataType.NETWORK:
            perf = Performance(self.deviceId, [perfTpe])
            perf.start(self.pkgName, callback=self.callback)
            time.sleep(3)
            perf.stop()
            perf_value = self.downflow, self.upflow
        else:
            perf = iosP.Performance(self.deviceId, [perfTpe])
            perf_value = perf.start(self.pkgName, callback=self.callback)
        return perf_value


class APM():
    """for python api"""

    def __init__(self, pkgName, deviceId='', platform='Android', surfaceview='true'):
        self.pkgName = pkgName
        self.deviceId = deviceId
        self.platform = platform
        self.surfaceview = surfaceview
        d._devicesCheck(pf=self.platform, id=self.deviceId, pkg=self.pkgName)

    def collectCpu(self):
        _cpu = CPU(self.pkgName, self.deviceId, self.platform)
        appCpuRate, systemCpuRate = _cpu.getCpuRate()
        result = {'appCpuRate': appCpuRate, 'systemCpuRate': systemCpuRate}
        logger.info(f'cpu: {result}')
        return result

    def collectMemory(self):
        _memory = MEM(self.pkgName, self.deviceId, self.platform)
        totalPass, nativePass, dalvikPass = _memory.getProcessMem()
        result = {'totalPass': totalPass, 'nativePass': nativePass, 'dalvikPass': dalvikPass}
        logger.info(f'memory: {result}')
        return result

    def collectBattery(self):
        _battery = Battery(self.deviceId, self.platform)
        final = _battery.getBattery()
        if self.platform == 'Android':
            result = {'level': final[0], 'temperature': final[1]}
        else:
            result = {'temperature': final[0], 'current': final[1], 'voltage': final[2], 'power': final[3]}
        logger.info(f'battery: {result}')
        return result

    def collectFlow(self):
        _flow = Flow(self.pkgName, self.deviceId, self.platform)
        upFlow, downFlow = _flow.getNetWorkData()
        result = {'upFlow': upFlow, 'downFlow': downFlow}
        logger.info(f'network: {result}')
        return result

    def collectFps(self):
        _fps = FPS(self.pkgName, self.deviceId, self.platform, self.surfaceview)
        fps, jank = _fps.getFPS()
        result = {'fps': fps, 'jank': jank}
        logger.info(f'fps: {result}')
        return result
