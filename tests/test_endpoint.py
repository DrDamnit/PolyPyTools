import unittest
from unittest_data_provider import data_provider
from poly_py_tools.pjsip_endpoint import Endpoint


class TestEndpoint(unittest.TestCase):

    provider_test_init = lambda :(
        #section                                                                                                                                                                                   expected_attributes
        (["[1234]", "100rel=Jyl5aQ2zp0VCQwUA", "aggregate_mwi=uMuYIQnX", "allow=RadaiCnMtKfDef", "aors=nnj63k", "auth=RtK1MwZD6", "callerid=T9n", "callerid_privacy=tOeiVAvTp61mx", "callerid_tag=hjuHGReXzyMIBVqzeIf", "context=2NRpB", "direct_media_glare_mitigation=TXoZEhoqp5", "direct_media_method=ayF", "connected_line_method=VVe4GoxMG3ByJY5", "direct_media=zYEnS3aZwkwVM", "disable_direct_media_on_nat=6NClLUwI2OV9N", "disallow=3hgsB1YrOA2K9dgsAxer", "dtmf_mode=haJA4q9", "media_address=g4oHrspWAWOUAv", "force_rport=KL1BSA8sxIHEjIJrH", "ice_support=6EZ7K6M0f", "identify_by=sHT5LoSUL0JI96561Ym", "redirect_method=enBAGEH", "mailboxes=NPD", "moh_suggest=Ay800ZGIR4Sx3cn", "outbound_auth=BWmM9N1UynmWkYV4cwd2", "outbound_proxy=1KnxgfT", "rewrite_contact=kbyf1WV2x0B1Uew", "rtp_ipv6=rmIkmzMONfmA", "rtp_symmetric=eTYnUOegdnyJHk5", "send_diversion=9NATl", "send_pai=G4xN4a", "send_rpid=PnC5WqSWEQ6jsuPFN", "timers_min_se=sPP", "timers=0F38S2kevvIiyo", "timers_sess_expires=USNkosRLJ", "transport=wUufsy6C9FI7x", "trust_id_inbound=SmGFqxXpPT", "trust_id_outbound=TwEa5bzZPYsae9zuu", "type=mCP", "use_ptime=TaXY5GNLQhNa2I", "use_avpf=6YeQ16kd4", "force_avp=pVDffsVStBi", "media_use_received_transport=c1I", "media_encryption=DfgunEGr46MG", "inband_progress=oQD", "call_group=QzHz0t3X7Xgy5PaYV", "pickup_group=RYGg7aLIs6TJCifJf", "named_call_group=zPehn28V92sgS", "named_pickup_group=63dtH9FiDWQ4gn9cBmo", "device_state_busy_at=PpA9Zo0on5qquH", "t38_udptl=w280yj", "t38_udptl_ec=Q5g4Wk3u40GLC4", "t38_udptl_maxdatagram=h09FAJ3J", "fax_detect=CafruWUb9sdosqQnt", "t38_udptl_nat=qH0usAmG45BhicuA5G3", "t38_udptl_ipv6=ABRzOi0FCvg", "tone_zone=jOgC3Znh", "language=i5NsRW9wA", "one_touch_recording=rPVx", "record_on_feature=9UqyhzZL5Y3JGiGCI", "record_off_feature=L4LxqiSfWVbjtjFhTO", "rtp_engine=KuGAiiojWJq2SfLaBl", "allow_transfer=bmoLg9W6", "sdp_owner=kcw7z", "sdp_session=rsA6X", "tos_audio=o07hJCtWhiN8VzYVzVVy", "tos_video=rpTk1Slswv9", "cos_audio=MCe8aReDnGZ3KW8", "cos_video=oEAAk7bln", "allow_subscribe=nKlS3SzJf", "sub_min_expiry=ZuiLPJTaQy36Pgm9YgiQ", "from_user=XnjbEqf5Lc9", "mwi_from_user=KaZRECvQOtTnz", "from_domain=uGGZVBgzdQ", "dtls_verify=xFqxevOVHTWNGbY", "dtls_rekey=oS8ETR", "dtls_cert_file=XI1SGYC5", "dtls_private_key=lKs9zUzh50NJhuA6oE0", "dtls_cipher=bnvQRwE", "dtls_ca_file=1XMI9RB", "dtls_ca_path=LaLkcspFAcU", "dtls_setup=envEaRPuFwcX", "dtls_fingerprint=deRrBNCxnL0QAOrF", "srtp_tag_32=4qJ", "set_var=kN4ldR0gdk", "message_context=9WMjdjhs7pZm", "accountcode=weQrrYS4PAVg0yAd6uiw"], {"rel_100":"Jyl5aQ2zp0VCQwUA", "aggregate_mwi":"uMuYIQnX", "allow":"RadaiCnMtKfDef", "aors":"nnj63k", "auth":"RtK1MwZD6", "callerid":"T9n", "callerid_privacy":"tOeiVAvTp61mx", "callerid_tag":"hjuHGReXzyMIBVqzeIf", "context":"2NRpB", "direct_media_glare_mitigation":"TXoZEhoqp5", "direct_media_method":"ayF", "connected_line_method":"VVe4GoxMG3ByJY5", "direct_media":"zYEnS3aZwkwVM", "disable_direct_media_on_nat":"6NClLUwI2OV9N", "disallow":"3hgsB1YrOA2K9dgsAxer", "dtmf_mode":"haJA4q9", "media_address":"g4oHrspWAWOUAv", "force_rport":"KL1BSA8sxIHEjIJrH", "ice_support":"6EZ7K6M0f", "identify_by":"sHT5LoSUL0JI96561Ym", "redirect_method":"enBAGEH", "mailboxes":"NPD", "moh_suggest":"Ay800ZGIR4Sx3cn", "outbound_auth":"BWmM9N1UynmWkYV4cwd2", "outbound_proxy":"1KnxgfT", "rewrite_contact":"kbyf1WV2x0B1Uew", "rtp_ipv6":"rmIkmzMONfmA", "rtp_symmetric":"eTYnUOegdnyJHk5", "send_diversion":"9NATl", "send_pai":"G4xN4a", "send_rpid":"PnC5WqSWEQ6jsuPFN", "timers_min_se":"sPP", "timers":"0F38S2kevvIiyo", "timers_sess_expires":"USNkosRLJ", "transport":"wUufsy6C9FI7x", "trust_id_inbound":"SmGFqxXpPT", "trust_id_outbound":"TwEa5bzZPYsae9zuu", "type":"mCP", "use_ptime":"TaXY5GNLQhNa2I", "use_avpf":"6YeQ16kd4", "force_avp":"pVDffsVStBi", "media_use_received_transport":"c1I", "media_encryption":"DfgunEGr46MG", "inband_progress":"oQD", "call_group":"QzHz0t3X7Xgy5PaYV", "pickup_group":"RYGg7aLIs6TJCifJf", "named_call_group":"zPehn28V92sgS", "named_pickup_group":"63dtH9FiDWQ4gn9cBmo", "device_state_busy_at":"PpA9Zo0on5qquH", "t38_udptl":"w280yj", "t38_udptl_ec":"Q5g4Wk3u40GLC4", "t38_udptl_maxdatagram":"h09FAJ3J", "fax_detect":"CafruWUb9sdosqQnt", "t38_udptl_nat":"qH0usAmG45BhicuA5G3", "t38_udptl_ipv6":"ABRzOi0FCvg", "tone_zone":"jOgC3Znh", "language":"i5NsRW9wA", "one_touch_recording":"rPVx", "record_on_feature":"9UqyhzZL5Y3JGiGCI", "record_off_feature":"L4LxqiSfWVbjtjFhTO", "rtp_engine":"KuGAiiojWJq2SfLaBl", "allow_transfer":"bmoLg9W6", "sdp_owner":"kcw7z", "sdp_session":"rsA6X", "tos_audio":"o07hJCtWhiN8VzYVzVVy", "tos_video":"rpTk1Slswv9", "cos_audio":"MCe8aReDnGZ3KW8", "cos_video":"oEAAk7bln", "allow_subscribe":"nKlS3SzJf", "sub_min_expiry":"ZuiLPJTaQy36Pgm9YgiQ", "from_user":"XnjbEqf5Lc9", "mwi_from_user":"KaZRECvQOtTnz", "from_domain":"uGGZVBgzdQ", "dtls_verify":"xFqxevOVHTWNGbY", "dtls_rekey":"oS8ETR", "dtls_cert_file":"XI1SGYC5", "dtls_private_key":"lKs9zUzh50NJhuA6oE0", "dtls_cipher":"bnvQRwE", "dtls_ca_file":"1XMI9RB", "dtls_ca_path":"LaLkcspFAcU", "dtls_setup":"envEaRPuFwcX", "dtls_fingerprint":"deRrBNCxnL0QAOrF", "srtp_tag_32":"4qJ", "set_var":"kN4ldR0gdk", "message_context":"9WMjdjhs7pZm", "accountcode":"weQrrYS4PAVg0yAd6uiw"}),
    )

    provider_test_process_exceptions = lambda : (
        (["[1234]", "100rel=Jyl5aQ2zp0VCQwUA", "aggregate_mwi=uMuYIQnX", "allow=RadaiCnMtKfDef", "aors=nnj63k", "auth=RtK1MwZD6", "callerid=T9n", "callerid_privacy=tOeiVAvTp61mx", "callerid_tag=hjuHGReXzyMIBVqzeIf", "context=2NRpB", "direct_media_glare_mitigation=TXoZEhoqp5", "direct_media_method=ayF", "connected_line_method=VVe4GoxMG3ByJY5", "direct_media=zYEnS3aZwkwVM", "disable_direct_media_on_nat=6NClLUwI2OV9N", "disallow=3hgsB1YrOA2K9dgsAxer", "dtmf_mode=haJA4q9", "media_address=g4oHrspWAWOUAv", "force_rport=KL1BSA8sxIHEjIJrH", "ice_support=6EZ7K6M0f", "identify_by=sHT5LoSUL0JI96561Ym", "redirect_method=enBAGEH", "mailboxes=NPD", "moh_suggest=Ay800ZGIR4Sx3cn", "outbound_auth=BWmM9N1UynmWkYV4cwd2", "outbound_proxy=1KnxgfT", "rewrite_contact=kbyf1WV2x0B1Uew", "rtp_ipv6=rmIkmzMONfmA", "rtp_symmetric=eTYnUOegdnyJHk5", "send_diversion=9NATl", "send_pai=G4xN4a", "send_rpid=PnC5WqSWEQ6jsuPFN", "timers_min_se=sPP", "timers=0F38S2kevvIiyo", "timers_sess_expires=USNkosRLJ", "transport=wUufsy6C9FI7x", "trust_id_inbound=SmGFqxXpPT", "trust_id_outbound=TwEa5bzZPYsae9zuu", "type=mCP", "use_ptime=TaXY5GNLQhNa2I", "use_avpf=6YeQ16kd4", "force_avp=pVDffsVStBi", "media_use_received_transport=c1I", "media_encryption=DfgunEGr46MG", "inband_progress=oQD", "call_group=QzHz0t3X7Xgy5PaYV", "pickup_group=RYGg7aLIs6TJCifJf", "named_call_group=zPehn28V92sgS", "named_pickup_group=63dtH9FiDWQ4gn9cBmo", "device_state_busy_at=PpA9Zo0on5qquH", "t38_udptl=w280yj", "t38_udptl_ec=Q5g4Wk3u40GLC4", "t38_udptl_maxdatagram=h09FAJ3J", "fax_detect=CafruWUb9sdosqQnt", "t38_udptl_nat=qH0usAmG45BhicuA5G3", "t38_udptl_ipv6=ABRzOi0FCvg", "tone_zone=jOgC3Znh", "language=i5NsRW9wA", "one_touch_recording=rPVx", "record_on_feature=9UqyhzZL5Y3JGiGCI", "record_off_feature=L4LxqiSfWVbjtjFhTO", "rtp_engine=KuGAiiojWJq2SfLaBl", "allow_transfer=bmoLg9W6", "sdp_owner=kcw7z", "sdp_session=rsA6X", "tos_audio=o07hJCtWhiN8VzYVzVVy", "tos_video=rpTk1Slswv9", "cos_audio=MCe8aReDnGZ3KW8", "cos_video=oEAAk7bln", "allow_subscribe=nKlS3SzJf", "sub_min_expiry=ZuiLPJTaQy36Pgm9YgiQ", "from_user=XnjbEqf5Lc9", "mwi_from_user=KaZRECvQOtTnz", "from_domain=uGGZVBgzdQ", "dtls_verify=xFqxevOVHTWNGbY", "dtls_rekey=oS8ETR", "dtls_cert_file=XI1SGYC5", "dtls_private_key=lKs9zUzh50NJhuA6oE0", "dtls_cipher=bnvQRwE", "dtls_ca_file=1XMI9RB", "dtls_ca_path=LaLkcspFAcU", "dtls_setup=envEaRPuFwcX", "dtls_fingerprint=deRrBNCxnL0QAOrF", "srtp_tag_32=4qJ", "set_var=kN4ldR0gdk", "message_context=9WMjdjhs7pZm", "accountcode=weQrrYS4PAVg0yAd6uiw"], ["[1234]", "rel_100=Jyl5aQ2zp0VCQwUA", "aggregate_mwi=uMuYIQnX", "allow=RadaiCnMtKfDef", "aors=nnj63k", "auth=RtK1MwZD6", "callerid=T9n", "callerid_privacy=tOeiVAvTp61mx", "callerid_tag=hjuHGReXzyMIBVqzeIf", "context=2NRpB", "direct_media_glare_mitigation=TXoZEhoqp5", "direct_media_method=ayF", "connected_line_method=VVe4GoxMG3ByJY5", "direct_media=zYEnS3aZwkwVM", "disable_direct_media_on_nat=6NClLUwI2OV9N", "disallow=3hgsB1YrOA2K9dgsAxer", "dtmf_mode=haJA4q9", "media_address=g4oHrspWAWOUAv", "force_rport=KL1BSA8sxIHEjIJrH", "ice_support=6EZ7K6M0f", "identify_by=sHT5LoSUL0JI96561Ym", "redirect_method=enBAGEH", "mailboxes=NPD", "moh_suggest=Ay800ZGIR4Sx3cn", "outbound_auth=BWmM9N1UynmWkYV4cwd2", "outbound_proxy=1KnxgfT", "rewrite_contact=kbyf1WV2x0B1Uew", "rtp_ipv6=rmIkmzMONfmA", "rtp_symmetric=eTYnUOegdnyJHk5", "send_diversion=9NATl", "send_pai=G4xN4a", "send_rpid=PnC5WqSWEQ6jsuPFN", "timers_min_se=sPP", "timers=0F38S2kevvIiyo", "timers_sess_expires=USNkosRLJ", "transport=wUufsy6C9FI7x", "trust_id_inbound=SmGFqxXpPT", "trust_id_outbound=TwEa5bzZPYsae9zuu", "type=mCP", "use_ptime=TaXY5GNLQhNa2I", "use_avpf=6YeQ16kd4", "force_avp=pVDffsVStBi", "media_use_received_transport=c1I", "media_encryption=DfgunEGr46MG", "inband_progress=oQD", "call_group=QzHz0t3X7Xgy5PaYV", "pickup_group=RYGg7aLIs6TJCifJf", "named_call_group=zPehn28V92sgS", "named_pickup_group=63dtH9FiDWQ4gn9cBmo", "device_state_busy_at=PpA9Zo0on5qquH", "t38_udptl=w280yj", "t38_udptl_ec=Q5g4Wk3u40GLC4", "t38_udptl_maxdatagram=h09FAJ3J", "fax_detect=CafruWUb9sdosqQnt", "t38_udptl_nat=qH0usAmG45BhicuA5G3", "t38_udptl_ipv6=ABRzOi0FCvg", "tone_zone=jOgC3Znh", "language=i5NsRW9wA", "one_touch_recording=rPVx", "record_on_feature=9UqyhzZL5Y3JGiGCI", "record_off_feature=L4LxqiSfWVbjtjFhTO", "rtp_engine=KuGAiiojWJq2SfLaBl", "allow_transfer=bmoLg9W6", "sdp_owner=kcw7z", "sdp_session=rsA6X", "tos_audio=o07hJCtWhiN8VzYVzVVy", "tos_video=rpTk1Slswv9", "cos_audio=MCe8aReDnGZ3KW8", "cos_video=oEAAk7bln", "allow_subscribe=nKlS3SzJf", "sub_min_expiry=ZuiLPJTaQy36Pgm9YgiQ", "from_user=XnjbEqf5Lc9", "mwi_from_user=KaZRECvQOtTnz", "from_domain=uGGZVBgzdQ", "dtls_verify=xFqxevOVHTWNGbY", "dtls_rekey=oS8ETR", "dtls_cert_file=XI1SGYC5", "dtls_private_key=lKs9zUzh50NJhuA6oE0", "dtls_cipher=bnvQRwE", "dtls_ca_file=1XMI9RB", "dtls_ca_path=LaLkcspFAcU", "dtls_setup=envEaRPuFwcX", "dtls_fingerprint=deRrBNCxnL0QAOrF", "srtp_tag_32=4qJ", "set_var=kN4ldR0gdk", "message_context=9WMjdjhs7pZm", "accountcode=weQrrYS4PAVg0yAd6uiw"]),
    )

    @data_provider(provider_test_process_exceptions)
    def test_process_exceptions(self, section, expected_result_section):
        endpoint = Endpoint(section)
        endpoint.process_exceptions()

        for i in range(1, len(expected_result_section)):
            self.assertEqual(expected_result_section[i], endpoint.section[i])

    @data_provider(provider_test_init)
    def test_init(self, section, expected_attributes):

        endpoint = Endpoint(section)
        self.assertEqual(section, endpoint.section)

        endpoint.set_attributes()

        for attribute in expected_attributes:
            expected_value = expected_attributes[attribute]
            actual_value = getattr(endpoint, attribute)
            self.assertEqual(expected_value, actual_value, "endpoint.{} should be {}. Got {} instead.".format(attribute, expected_value, actual_value))


if __name__ == '__main__':
    unittest.main()