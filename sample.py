####################################################################################################
#
#
#CODE TO VERIFY BGP SPEAKER IS ABLE TO SET AND ADVERTISE THE COMMUNITY ATTRIBUTE TO THE BGP NEIGHBOR.
#
#
#
####################################################################################################

import os
import sys
import time
import re
import telnetlib





class VerifyBGPCommunity:

##############Perform configuration on the router############################################### 
    
    def  ConfigRouterforBGP(self, BGPRoueBGPDUT1ConfSet25, BGPRoueBGPDUT2ConfSet25):
        
         try:
             host1=paf.LCTIPDUT1
             host4=paf.LCTIPDUT4
             
             

             tn1=cmObj.telnet_dut(host1)
             time.sleep(3)
             stObj.setConfigurationOnRoutedPort(tn1, BGPRoueBGPDUT1ConfSet25)
             time.sleep(3)
             tn4=cmObj.telnet_dut(host4)
             time.sleep(3)
             stObj.setConfigurationOnRoutedPort(tn4, BGPRoueBGPDUT2ConfSet25)
             
             
         except Exception as e:
             raise RuntimeError("BGP config could not be performed on " ,host1," and ", host4)

##########################Show command on the router ##########################################

    def ShowCommand(self, BGPRoueBGPShwCmdSet25):

        try:
            host1=paf.LCTIPDUT1
            host4=paf.LCTIPDUT4
            
        
            tn1=cmObj.telnet_dut(host1)
            time.sleep(3)
            stObj.captureShowCommandOutput(tn1, BGPRoueBGPShwCmdSet25)
            tn4=cmObj.telnet_dut(host4)
            time.sleep(3)
            stObj.captureShowCommandOutput(tn4, BGPRoueBGPShwCmdSet25)
            time.sleep(3)
        except:
            print("Show command config could not be performed for Static configuration for " ,host1, " and ", host4)
         
####################Perform validation if BGP neighborship is established and static and coneected routes are redistributed#################################################################

    def VerfyBGPNeighborShip(self, BGPRoueBGPShwCmdSet25, BGPRoueBGPShwCmd2Set25, BGPRoueBGPDUTStr1VldnSet25, BGPRoueBGPDUTStr2VldnSet25, BGPRoueBGPDUT1Str3VldnSet25, BGPRoueBGPDUT2Str4VldnSet25,
                             BGPRoueBGPDUT1RemComSet25, BGPRoueBGPDUT2Str5VldnSet25, BGPRoueBGPDUT2RemComSet25,BGPRoueBGPDUT1ClnUPSet25, BGPRoueBGPDUT2ClnUpSet25):

        host1=paf.LCTIPDUT1
        host4=paf.LCTIPDUT4
        

        time.sleep(3)
        

        sr1 = BGPRoueBGPDUTStr1VldnSet25 #'Established'

        
        tn1=cmObj.telnet_dut(host1)
        time.sleep(2)
        output1 = stObj.validateDUT(tn1, BGPRoueBGPShwCmdSet25)
        time.sleep(3)
        print(output1)

        tn4=cmObj.telnet_dut(host4)
        time.sleep(2)
        output2 = stObj.validateDUT(tn4, BGPRoueBGPShwCmdSet25)
        time.sleep(3)
        print(output2)

        
        validation1 = output1.count(sr1)
        validation2 = output2.count(sr1)
        
        
        print(validation1,validation2)

        try:
           if validation1 == 2 and validation2 == 2:
               print("PASS: BGP successfully established between",host1,host4)
               
                        
           else:
               print("FAIL: BGP successfully established between",host1,host4)
               raise RuntimeError("FAIL: TC validation for BGP neighborship and Route-map configuration failed ",host1,host4)

        except Exception as e:
            print("FAIL: TC validation for BGP neighborship establishement failed ",host1,host4)
            raise RuntimeError("FAIL: TC validation for BGP neighborship establishement failed ",host1,host4)
        
        finally:
            BGP.VerifyBgpRouteMapAndCommunity(BGPRoueBGPShwCmdSet25, BGPRoueBGPShwCmd2Set25, BGPRoueBGPDUTStr1VldnSet25, BGPRoueBGPDUTStr2VldnSet25, BGPRoueBGPDUT1Str3VldnSet25,
                                              BGPRoueBGPDUT2Str4VldnSet25, BGPRoueBGPDUT1RemComSet25, BGPRoueBGPDUT2Str5VldnSet25, BGPRoueBGPDUT2RemComSet25,BGPRoueBGPDUT1ClnUPSet25,
                                              BGPRoueBGPDUT2ClnUpSet25)

        
############ Verify BGP route-map and community ####################

    def VerifyBgpRouteMapAndCommunity(self, BGPRoueBGPShwCmdSet25, BGPRoueBGPShwCmd2Set25, BGPRoueBGPDUTStr1VldnSet25, BGPRoueBGPDUTStr2VldnSet25, BGPRoueBGPDUT1Str3VldnSet25,
                                      BGPRoueBGPDUT2Str4VldnSet25,  BGPRoueBGPDUT1RemComSet25, BGPRoueBGPDUT2Str5VldnSet25, BGPRoueBGPDUT2RemComSet25,BGPRoueBGPDUT1ClnUPSet25,
                                      BGPRoueBGPDUT2ClnUpSet25):

        host1=paf.LCTIPDUT1
        host4=paf.LCTIPDUT4

        tn1=cmObj.telnet_dut(host1)
        time.sleep(2)
        output1 = stObj.validateDUT(tn1, BGPRoueBGPShwCmd2Set21)
        print (output1)

        time.sleep(3)

        tn4=cmObj.telnet_dut(host4)
        time.sleep(3)
        output2 = stObj.validateDUT(tn4, BGPRoueBGPShwCmd2Set21)
        print (output2)
        
        time.sleep(3)
    
        sr1 = BGPRoueBGPDUTStr2VldnSet25  #'Route-map community, Permit, Sequence 1'
        sr2 = BGPRoueBGPDUT1Str3VldnSet25 #'30.30.30.30  200          automatic enable   standard,extended'
        sr3 = BGPRoueBGPDUT2Str4VldnSet25 #'20.20.20.20  100          automatic enable   standard,extended'



        

        print("Validation String ", sr1, " used")
        print("Validation String ", sr2, " used")
        print("Validation String ", sr3, " used")

        
        validation1 = output1.count(sr1)
        validation2 = output2.count(sr1)
        validation3 = output1.count(sr2)
        validation4 = output2.count(sr3)

        
        print (validation1, validation2, validation3, validation4)
        
        
        time.sleep(2)
        
        try:
           if validation1 == 1 and validation2 == 1 and validation3 == 1 and validation4 == 1 :
               print ("PASS: Route-map configured successfully for ",host1)
               print ("PASS: Route-map configured successfully for ",host4)
               print ("PASS: Community configured successfully for ",host1)
               print ("PASS: Community configured successfully for ",host4)
               

           else:
               print("FAIL: Route map and community not configured for ", host1, "and", host4)
            
               raise RuntimeError("FAIL: Route map and community not configured for ", host1, "and", host4))

        except Exception as e:
           raise RuntimeError("FAIL: Route map and community not configured for ", host1, "and", host4))

     
        finally:
            BGP.VerifyCommunityRemoval(BGPRoueBGPShwCmdSet25, BGPRoueBGPShwCmd2Set25, BGPRoueBGPDUTStr1VldnSet25, BGPRoueBGPDUTStr2VldnSet25, BGPRoueBGPDUT1Str3VldnSet25,
                             BGPRoueBGPDUT2Str4VldnSet25,  BGPRoueBGPDUT1RemComSet25, BGPRoueBGPDUT2Str5VldnSet25, BGPRoueBGPDUT2RemComSet25,BGPRoueBGPDUT1ClnUPSet25,
                             BGPRoueBGPDUT2ClnUpSet25)
            
############Verify route-map removal ####################

    def VerifyCommunityRemoval(self, BGPRoueBGPShwCmdSet25, BGPRoueBGPShwCmd2Set25, BGPRoueBGPDUTStr1VldnSet25, BGPRoueBGPDUTStr2VldnSet25, BGPRoueBGPDUT1Str3VldnSet25,
                     BGPRoueBGPDUT2Str4VldnSet25,  BGPRoueBGPDUT1RemComSet25, BGPRoueBGPDUT2Str5VldnSet25, BGPRoueBGPDUT2RemComSet25,BGPRoueBGPDUT1ClnUPSet25,
                     BGPRoueBGPDUT2ClnUpSet25):

        try:
            host1=paf.LCTIPDUT1
            host4=paf.LCTIPDUT4

            tn1=cmObj.telnet_dut(host1)
            time.sleep(2)
            output1 = stObj.validateDUT(tn1, BGPRoueBGPDUT1RemComSet25)
            print (output1)

            time.sleep(3)
    
            sr1 = BGPRoueBGPDUT2RemComSet25   #'community'

            print("Validation String ", sr1, " used")
        

        
            validation1 = output1.count(sr1)

            if validation1 == 0:
                print("PASS:Community has been removed successfully")
            else:
                print("FAIL: Community not removed successfully")
                raise RuntimeError("FAIL: Community not removed successfully")
        except:
            raise RuntimeError("TC validation failed for community removal for " ,host1, " and ", host4)
        finally:
            BGP.VerifyCommunityPrefixinRouTable(BGPRoueBGPShwCmdSet25, BGPRoueBGPShwCmd2Set25, BGPRoueBGPDUTStr1VldnSet25, BGPRoueBGPDUTStr2VldnSet25, BGPRoueBGPDUT1Str3VldnSet25,
                                                BGPRoueBGPDUT2Str4VldnSet25,  BGPRoueBGPDUT1RemComSet25, BGPRoueBGPDUT2Str5VldnSet25, BGPRoueBGPDUT2RemComSet25,BGPRoueBGPDUT1ClnUPSet25,
                                                BGPRoueBGPDUT2ClnUpSet25)
            

############Verify route-map removal ####################

    def VerifyCommunityPrefixinRouTable(self, BGPRoueBGPShwCmdSet25, BGPRoueBGPShwCmd2Set25, BGPRoueBGPDUTStr1VldnSet25, BGPRoueBGPDUTStr2VldnSet25, BGPRoueBGPDUT1Str3VldnSet25,
                                        BGPRoueBGPDUT2Str4VldnSet25, BGPRoueBGPDUT1RemComSet25, BGPRoueBGPDUT2Str5VldnSet25, BGPRoueBGPDUT2RemComSet25, BGPRoueBGPDUT1ClnUPSet25,
                                        BGPRoueBGPDUT2ClnUpSet25):

        try:
            host1=paf.LCTIPDUT1
            host4=paf.LCTIPDUT4

            tn4=cmObj.telnet_dut(host4)
            time.sleep(2)
            output1 = stObj.validateDUT(tn4, BGPRoueBGPDUT2Str5VldnSet25)
            print (output1)

            time.sleep(3)
    
            sr1 = BGPRoueBGPDUT2RemComSet25  #'community'

            print("Validation String ", sr1, " used")
        
            validation1 = output1.count(sr1)

            if validation1 == 1:
                print("PASS:Community attribute should be tagged in BGP routing table successfully")
            else:
                print("FAIL: Community attribute not tagged in BGP routing table successfully. Please refer bug Bug 20191 ")
                raise RuntimeError("FAIL: Community attribute not tagged in BGP routing table successfully. Please refer bug Bug 20191 ")
            
        except:
            raise RuntimeError("FAIL: Community attribute not tagged in BGP routing table successfully. Please refer bug Bug 20191 ")
        
        finally:
            BGP.CleanupRouter(BGPRoueBGPDUT1ClnUPSet25, BGPRoueBGPDUT2ClnUpSet25)
        
##############################Perform Cleanup on all DUT's#############################################

        
    def CleanupRouter(self, BGPRoueBGPDUT1ClnUPSet25, BGPRoueBGPDUT2ClnUpSet25):

        try:
            host1=paf.LCTIPDUT1
            host4=paf.LCTIPDUT4       

            tn1=cmObj.telnet_dut(host1)
            time.sleep(3)
            stObj.cleanup(tn1, BGPRoueBGPDUT1ClnUPSet25)
            time.sleep(3)
            tn4=cmObj.telnet_dut(host4)
            time.sleep(3)
            stObj.cleanup(tn4, BGPRoueBGPDUT2ClnUpSet25)
            
        except:
            print("Cleanup command config could not be performed on " ,host1, " and ", host4)
            raise RuntimeError("Cleanup command config could not be performed on " ,host1, " and ", host4)




BGP = VerifyBGPCommunity()

def main(BGPRoueBGPDUT1ConfSet25, BGPRoueBGPDUT2ConfSet25, BGPRoueBGPShwCmdSet25, BGPRoueBGPShwCmd2Set25, BGPRoueBGPDUTStr1VldnSet25, BGPRoueBGPDUTStr2VldnSet25,
                      BGPRoueBGPDUT1Str3VldnSet25, BGPRoueBGPDUT2Str4VldnSet25, BGPRoueBGPDUT1RemComSet25, BGPRoueBGPDUT2Str5VldnSet25, BGPRoueBGPDUT2RemComSet25,
                      BGPRoueBGPDUT1ClnUPSet25, BGPRoueBGPDUT2ClnUpSet25):

    BGP.ConfigRouterforBGP(BGPRoueBGPDUT1ConfSet25, BGPRoueBGPDUT2ConfSet25)
    BGP.ShowCommand(BGPRoueBGPShwCmdSet25)
    BGP.VerfyBGPNeighborShip(BGPRoueBGPShwCmdSet25, BGPRoueBGPShwCmd2Set25, BGPRoueBGPDUTStr1VldnSet25, BGPRoueBGPDUTStr2VldnSet25, BGPRoueBGPDUT1Str3VldnSet25, BGPRoueBGPDUT2Str4VldnSet25,
                             BGPRoueBGPDUT1RemComSet25, BGPRoueBGPDUT2Str5VldnSet25, BGPRoueBGPDUT2RemComSet25,BGPRoueBGPDUT1ClnUPSet25, BGPRoueBGPDUT2ClnUpSet25)
    #BGP.CleanupRouter(BGPRouiBGPDUT1ClnUpSet22, BGPRouiBGPDUT2ClnUpSet22)
