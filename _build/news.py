# -*- coding: utf-8 -*-
# 규제 뉴스 데이터. 출처는 규제기관·공공기관·표준기구의 공식 발표만 사용한다.
# src: (한국어 이름, 영어 이름, URL)
UPDATED = "2026-11-19"

REGIONS = {
    "kr": {"ko": "한국", "en": "Korea"},
    "eu": {"ko": "EU", "en": "EU"},
    "us": {"ko": "미국", "en": "US"},
    "cn": {"ko": "중국", "en": "China"},
    "uk": {"ko": "영국", "en": "UK"},
    "intl": {"ko": "국제", "en": "International"},
    "jp": {"ko": "일본", "en": "Japan"},
    "au": {"ko": "호주", "en": "Australia"},
    "ca": {"ko": "캐나다", "en": "Canada"},
    "br": {"ko": "브라질", "en": "Brazil"},
    "me": {"ko": "중동", "en": "Middle East"},
    "sea": {"ko": "동남아", "en": "Southeast Asia"},
    "ar": {"ko": "아르헨티나", "en": "Argentina"},
    "il": {"ko": "이스라엘", "en": "Israel"},
    "ke": {"ko": "케냐", "en": "Kenya"},
    "mx": {"ko": "멕시코", "en": "Mexico"},
    "za": {"ko": "남아공", "en": "South Africa"},
    "tw": {"ko": "대만", "en": "Taiwan"},
}

NEWS = [
 {
  "slug": "mdcg-2026-6", "date": "2026-11-03", "region": "eu", "svc": "technical-documentation",
  "ko": {
   "title": "MDCG, 희소 체외진단기기의 임상 근거 지침(MDCG 2026-6) 발간",
   "sum": "유럽집행위원회가 2026년 11월 3일 희소 체외진단기기(orphan IVD)의 임상 근거에 관한 MDCG 지침을 공개했습니다.",
   "points": [
    "희소 IVD로 인정받기 위해 충족해야 하는 기준을 제시합니다.",
    "IVD의 성능은 과학적 타당성, 분석적 성능, 임상적 성능으로 입증하는데, 환자 집단이 매우 작은 희소 IVD에 이를 어떻게 적용할지 다룹니다.",
    "임상 근거는 안전성, 성능, 의도한 임상적 이점을 자격 있는 평가자가 판단할 수 있는 양과 질의 데이터에 기반해야 한다고 설명합니다.",
    "문서에는 희소 IVD를 자체 제조하는 EU 보건기관을 위한 안내 문구도 있습니다.",
    "희소 의료기기(MD)의 임상평가는 별도 문서인 MDCG 2024-10(2024년 6월)에서 다룹니다.",
   ],
  },
  "en": {
   "title": "MDCG publishes guidance on clinical evidence for orphan IVDs (MDCG 2026-6)",
   "sum": "On 3 November 2026 the European Commission published an MDCG guidance document on clinical evidence for orphan in vitro diagnostic medical devices.",
   "points": [
    "It sets out the criteria a device must meet to qualify as an orphan IVD.",
    "IVD performance is shown through scientific validity, analytical performance and clinical performance. The guidance addresses how this applies to orphan IVDs, which serve very small patient populations.",
    "It explains that clinical evidence should rest on data of sufficient quantity and quality to allow a qualified assessment of safety, performance and intended clinical benefit.",
    "The document also includes a note for EU health institutions that manufacture orphan IVDs in-house.",
    "Clinical evaluation of orphan medical devices (not IVDs) is covered separately in MDCG 2024-10 (June 2024).",
   ],
  },
  "src": [
   ("유럽집행위원회 보건총국(DG SANTE) 공지", "European Commission, DG SANTE announcement", "https://health.ec.europa.eu/latest-updates/new-guidance-document-mdcg-2026-6-guidance-clinical-evidence-orphan-ivds-2026-11-03_en"),
   ("MDCG 2026-6 원문 (PDF)", "MDCG 2026-6 (PDF)", "https://health.ec.europa.eu/document/download/3c335d66-18db-4ab2-9fdd-fe552e897200_en?filename=mdcg_2026-6_en.pdf"),
   ("MDCG 2024-10 원문 (PDF)", "MDCG 2024-10 (PDF)", "https://health.ec.europa.eu/document/download/daa1fc59-9d2c-4e82-878e-d6fdf12ecd1a_en?filename=mdcg_2024-10_en.pdf"),
  ],
 },
 {
  "slug": "cn-gmp-2026", "date": "2026-11-02", "region": "cn", "svc": "qms",
  "ko": {
   "title": "중국 개정 의료기기 GMP 시행(11월 1일), NMPA는 점검 지침도 잇따라 공개",
   "sum": "2025년 11월에 공표된 개정 의료기기 생산질량관리규범(GMP)이 2026년 11월 1일부터 시행됩니다. NMPA는 이에 맞춘 점검 지도원칙을 9월과 11월에 발표했습니다.",
   "points": [
    "NMPA는 2025년 11월 4일 공고(2025년 제107호)로 개정 GMP를 발표했고, 2026년 11월 1일부터 시행하며 2014년 제64호 규범은 폐지됩니다.",
    "2026년 9월 15일 게시된 통지(국약감계관〔2026〕14호)가 GMP 점검 지도원칙을 시달했습니다. 11월 1일부터 생산허가 점검과 시판 후 감독점검은 개정 GMP를 기준으로 하고, 이 지도원칙으로 판정합니다.",
    "11월 1일 이전에 접수됐지만 현장 점검을 하지 않은 허가·변경·연장 신청은 11월 1일부터 개정 GMP로 점검합니다.",
    "무균, 이식, 체외진단시약, 맞춤형 의치, 독립 소프트웨어 의료기기는 개정 GMP와 해당 현행 부속서를 함께 충족해야 합니다. 해당 점검 지도원칙은 따로 개정해 발표한다고 밝혔습니다.",
    "독립 소프트웨어는 국약감계관〔2026〕17호(2026년 11월 2일 게시) '독립 소프트웨어 점검 지도원칙'이 별도로 나왔습니다. 11월 1일부터 시행되며 점검 항목은 203개(핵심 41, 주요 94, 일반 68)입니다.",
   ],
  },
  "en": {
   "title": "China's revised medical device GMP takes effect 1 November; NMPA issues inspection guidance",
   "sum": "The revised Good Manufacturing Practice for medical devices, announced in November 2025, applies from 1 November 2026. NMPA issued matching inspection guidelines in September and November.",
   "points": [
    "NMPA announced the revised GMP on 4 November 2025 (Announcement No. 107 of 2025). It applies from 1 November 2026 and replaces the 2014 GMP (No. 64).",
    "A notice posted on 15 September 2026 (Guo Yao Jian Xie Guan [2026] No. 14) issued the GMP inspection guidelines. From 1 November, production licence checks and post-market inspections follow the revised GMP and are judged under these guidelines.",
    "Licence, change and renewal applications accepted before 1 November but not yet inspected on site are inspected under the revised GMP from 1 November.",
    "Sterile, implantable, IVD reagent, custom-made denture and standalone software devices must meet both the revised GMP and the corresponding existing annex. The notice says the matching inspection guidelines will be revised and issued separately.",
    "For standalone software, a separate notice (Guo Yao Jian Xie Guan [2026] No. 17, posted 2 November 2026) issued the 'Standalone Software Inspection Guidelines'. They apply from 1 November and contain 203 items (41 key, 94 major, 68 general).",
   ],
  },
  "src": [
   ("국가약품감독관리국(NMPA) 개정 GMP 발표", "NMPA: revised GMP released", "https://www.nmpa.gov.cn/yaowen/ypjgyw/ylqxyw/20251104174018114.html"),
   ("중국 정부망: NMPA 공고 2025년 제107호 (규범 전문)", "gov.cn: NMPA Announcement No. 107 (full text)", "https://www.gov.cn/zhengce/zhengceku/202511/content_7047263.htm"),
   ("NMPA: GMP 점검 지도원칙 통지 (국약감계관〔2026〕14호)", "NMPA: GMP inspection guidelines notice (No. 14)", "https://www.nmpa.gov.cn/xxgk/fgwj/gzwj/gzwjylqx/20260915163938138.html"),
   ("상하이시 약품감독관리국: 독립 소프트웨어 점검 지도원칙 통지 (NMPA 문서 전재)", "Shanghai MPA: standalone software inspection notice (NMPA document)", "https://yjj.sh.gov.cn/qtgzwj/20261102/6b5c9fdcd7a54f71999c097efb5a7cc7.html"),
  ],
 },
 {
  "slug": "mdcg-2026-4-rev1", "date": "2026-10-30", "region": "eu", "svc": "technical-documentation",
  "ko": {
   "title": "MDCG 2026-4 개정 1판: 의무 사용 이후 EUDAMED의 SS(C)P 관리 방식",
   "sum": "유럽집행위원회가 2026년 10월 30일, EUDAMED 의무 사용 이후 안전·임상성능 요약서(SSCP)와 안전·성능 요약서(SSP) 관리 방식을 다룬 MDCG 입장문의 개정 1판을 공개했습니다.",
   "points": [
    "이 입장문은 2026년 6월에 처음 공개됐고, 10월 개정 1판이 나왔습니다.",
    "현재 SSCP와 SSP는 MDR 제32조 제1항, IVDR 제29조 제1항에 따라 인증기관이 인증서 정보를 등록할 때 올리도록 되어 있지만, 이 정책은 바뀌는 중이라고 설명합니다.",
    "SSCP 지침인 MDCG 2019-9 rev.1을 개정해 제조자에게 역할을 부여하는 방향으로 정리하고 있습니다.",
    "인증서 등록 때 SS(C)P 번역본을 EUDAMED에 올릴 필요는 없습니다.",
    "EUDAMED 테스트 환경(Playground)의 릴리스 노트에는 SS(C)P 등록 책임이 인증기관에서 제조자로 이전되고, 인증기관은 새 SS(C)P를 등록할 수 없다고 적혀 있습니다. 운영 환경 적용 시점은 EU 공식 공지로 확인해야 합니다.",
   ],
  },
  "en": {
   "title": "MDCG 2026-4 rev.1: managing SS(C)P in EUDAMED after mandatory use",
   "sum": "On 30 October 2026 the European Commission published revision 1 of the MDCG position paper on how the summary of safety and clinical performance (SSCP) and the summary of safety and performance (SSP) are managed in EUDAMED after mandatory use.",
   "points": [
    "The position paper was first published in June 2026; revision 1 followed in October.",
    "Today the SSCP and SSP are uploaded by the notified body when it registers certificate information under Article 32(1) MDR and Article 29(1) IVDR. The paper says this policy is evolving.",
    "The SSCP guidance MDCG 2019-9 rev.1 is being revised to give the manufacturer a role in this process.",
    "Certificate registration does not require uploading SS(C)P translations to EUDAMED.",
    "Release notes for the EUDAMED Playground (test environment) state that SS(C)P registration responsibility moves from notified bodies to manufacturers, and that notified bodies can no longer register new SS(C)Ps. Check official EU notices for when this applies in the live system.",
   ],
  },
  "src": [
   ("유럽집행위원회 보건총국(DG SANTE) 공지", "European Commission, DG SANTE announcement", "https://health.ec.europa.eu/latest-updates/new-revision-mdcg-position-paper-management-sscp-eudamed-after-mandatory-use-2026-10-30_en"),
   ("MDCG 2026-4 rev.1 원문 (PDF)", "MDCG 2026-4 rev.1 (PDF)", "https://health.ec.europa.eu/document/download/a80332cf-e9f0-4d45-8863-3d96e8c2a675_en?filename=mdcg_2026-4_en.pdf"),
   ("EUDAMED Playground 릴리스 노트", "EUDAMED Playground release notes", "https://webgate.ec.europa.eu/eudamed-play-help/en/files/EUDAMED%20-%20release%20notes.pdf"),
   ("MDCG 지침 문서 목록", "MDCG guidance documents list", "https://health.ec.europa.eu/medical-devices-sector/new-regulations/guidance-mdcg-endorsed-documents-and-other-guidance_en"),
  ],
 },
 {
  "slug": "kr-cybersecurity-guideline", "date": "2026-10-30", "region": "kr", "svc": "cybersecurity",
  "ko": {
   "title": "식약처, 의료기기 사이버보안 허가심사 가이드라인 개정",
   "sum": "식품의약품안전처가 2026년 10월 30일 보도참고자료로 「의료기기 사이버보안 허가심사 가이드라인」을 개정했다고 밝혔습니다.",
   "points": ["식약처가 10월 30일 보도참고자료(PDF·HWPX)를 게시했습니다.", "안내서 「의료기기의 사이버보안 허가·심사 가이드라인(민원인 안내서)」(등록번호 안내서-0995-06, 의료기기심사부, 발행일 2026년 10월 30일)의 개정 이력서에는 이번 개정의 주요 내용이 요구사항 국제조화(IA-04, IA-05), 명확화(SI-05, SI-07) 및 별첨 삭제로 기재되어 있습니다.", "바로 앞 개정본(안내서-0995-05, 2025년 1월 10일)의 주요 내용은 요구사항 시행시기 명확화로 기재되어 있습니다.", "2026년 1월 26일에는 의료기기·체외진단의료기기 허가·신고·심사 규정이 개정되어 사이버보안 심사자료 제출 근거가 정리됐습니다(별도 항목 참고)."],
   "check": "세부 내용은 안내서 원문에서 확인하세요.",
  },
  "en": {
   "title": "MFDS revises the cybersecurity review guideline for medical devices",
   "sum": "On 30 October 2026 the Ministry of Food and Drug Safety (MFDS) announced, in a press reference document, a revision of its guideline on cybersecurity review and approval of medical devices.",
   "points": ["MFDS posted the press reference document (PDF and HWPX) on 30 October.", "The revision history of the guidance \"Guideline on Cybersecurity Review and Approval of Medical Devices (guidance for applicants)\" (registration number 안내서-0995-06, Medical Device Evaluation Department, issued 30 October 2026) records the main content of this revision as international harmonization of requirements (IA-04, IA-05), clarification (SI-05, SI-07) and deletion of an appendix.", "The previous revision (안내서-0995-05, 10 January 2025) records its main content as clarifying when the requirements take effect.", "On 26 January 2026 the medical device and IVD approval rules were amended, clarifying the basis for submitting cybersecurity review data (see the separate item)."],
   "check": "Check the guidance original for details.",
  },
  "src": [
   ("식약처 보도참고자료 (2026-10-30)", "MFDS press reference (2026-10-30)", "https://mfds.go.kr/brd/m_99/view.do?seq=50456"),
   ("식약처 민원인 안내서: 의료기기의 사이버보안 허가·심사 가이드라인", "MFDS guideline page: cybersecurity review and approval of medical devices", "https://www.mfds.go.kr/brd/m_1060/view.do?seq=15625"),
   ("식약처 안내서 게시글: 의료기기의 사이버보안 허가·심사 가이드라인 개정(안내서-0995-06)", "MFDS guidance post: cybersecurity review and approval of medical devices, revision (안내서-0995-06)", "https://www.mfds.go.kr/brd/m_1060/view.do?seq=15987&srchFr=&srchTo=&srchWord=&srchTp=&itm_seq_1=0&itm_seq_2=0&multi_itm_seq=0&company_cd=&company_nm=&page=2"),
  ],
 },
 {
  "slug": "kr-professional-use-software", "date": "2026-09-30", "region": "kr", "svc": "digital-medical-products",
  "ko": {
   "title": "식약처, 전문가용 디지털의료기기소프트웨어 허가·심사 가이드라인 제정",
   "sum": "식약처가 2026년 9월 30일 「전문가용 디지털의료기기소프트웨어 허가·심사 가이드라인(민원인 안내서)」을 제정했다고 공지했습니다.",
   "points": [
    "등록번호는 안내서-1528-01, 담당 부서는 의료인공지능소프트웨어과입니다.",
    "같은 날 보도참고자료 「전문가용 디지털의료기기소프트웨어 허가심사 가이드라인 마련」도 게시됐습니다.",
    "함께 참고할 기존 문서로 의료기기 소프트웨어 허가·심사 가이드라인(2025년 5월 7일 개정)과 독립형 디지털의료기기소프트웨어 사용적합성 허가·심사 가이드라인(2025년 1월 24일)이 있습니다.",
   ],
   "check": "적용 대상 범위와 제출자료의 세부 요건은 가이드라인 원문에서 확인하세요.",
  },
  "en": {
   "title": "MFDS issues a guideline on approval of digital medical device software for professional use",
   "sum": "On 30 September 2026 MFDS notified the establishment of its guideline on review and approval of digital medical device software for professional use.",
   "points": [
    "The registration number is 안내서-1528-01 and the responsible division is the Medical AI Software Division.",
    "A press reference document with the same title was posted on the same day.",
    "Related existing documents include the medical device software approval guideline (revised 7 May 2025) and the usability guideline for standalone digital medical device software (24 January 2025).",
   ],
   "check": "Check the guideline itself for its scope and the detailed submission requirements.",
  },
  "src": [
   ("식약처 민원인 안내서: 전문가용 디지털의료기기소프트웨어 허가·심사 가이드라인", "MFDS guideline page", "https://www.mfds.go.kr/brd/m_1060/view.do?seq=15956"),
   ("식약처 보도참고자료 (2026-09-30)", "MFDS press reference (2026-09-30)", "https://mfds.go.kr/brd/m_99/view.do?seq=50381"),
  ],
 },
 {
  "slug": "kr-digital-quality-certification", "date": "2026-08-12", "region": "kr", "svc": "digital-medical-products",
  "ko": {
   "title": "식약처, 디지털의료기기 우수 관리체계 인증 가이드라인 제정",
   "sum": "식약처가 2026년 8월 12일 「디지털의료기기 우수 관리체계 인증 가이드라인(민원인 안내서)」을 제정했다고 공지했습니다.",
   "points": [
    "등록번호는 안내서-1516-01, 담당 부서는 디지털의료제품지원총괄과입니다.",
    "같은 날 게시된 보도참고자료의 제목은 「AI 디지털의료기기 우수 관리체계 인증 가이드라인 마련」입니다.",
    "디지털의료제품법(2025년 1월 24일 시행)에 따른 디지털의료기기 GMP 가이드라인은 2025년 11월 13일에 별도로 게시되어 있습니다.",
   ],
   "check": "인증 대상, 절차, 요건은 가이드라인 원문에서 확인하세요.",
  },
  "en": {
   "title": "MFDS issues a guideline on good management system certification for digital medical devices",
   "sum": "On 12 August 2026 MFDS notified the establishment of its guideline on good management system certification for digital medical devices.",
   "points": [
    "The registration number is 안내서-1516-01 and the responsible division is the Digital Medical Products Support Division.",
    "The press reference document posted the same day is titled 'MFDS prepares a good management system certification guideline for AI digital medical devices'.",
    "A separate GMP guideline for digital medical devices under the Digital Medical Products Act (in force since 24 January 2025) was posted on 13 November 2025.",
   ],
   "check": "Check the guideline itself for who is covered, the procedure and the requirements.",
  },
  "src": [
   ("식약처 민원인 안내서: 디지털의료기기 우수 관리체계 인증 가이드라인", "MFDS guideline page", "https://www.mfds.go.kr/brd/m_1060/view.do?seq=15905"),
   ("식약처 보도참고자료 (2026-08-12)", "MFDS press reference (2026-08-12)", "https://mfds.go.kr/brd/m_99/view.do?seq=50266"),
   ("식약처 민원인 안내서: 디지털의료기기 GMP 가이드라인", "MFDS guideline page: digital medical device GMP", "https://www.mfds.go.kr/brd/m_1060/view.do?seq=15756"),
  ],
 },
 {
  "slug": "eu-mdr-ivdr-revision", "date": "2026-07-28", "region": "eu", "svc": "technical-documentation",
  "ko": {
   "title": "EU MDR·IVDR 간소화 개정안, 유럽의회 보건위 초안 보고서와 수정안 단계",
   "sum": "유럽집행위원회가 2025년 12월 16일 MDR·IVDR 간소화 개정안을 제안했고, 유럽의회 보건위(SANT)는 2026년 6월 30일 초안 보고서를, 7월 28일 수정안을 올렸습니다.",
   "points": [
    "개정안(COM(2025)1023)은 MDR·IVDR과 함께 전문가 패널에 대한 EMA 지원 규정(EU 2022/123), AI법의 부속서 I 목록(EU 2024/1689)을 함께 고치는 안입니다. 목표는 규정을 간소화하고 부담을 줄이는 것입니다.",
    "유럽의회에서는 SANT가 주관 위원회이고 올리버 솅크(Oliver Schenk, EPP) 의원이 보고관입니다(2026년 2월 13일 지명). 초안 보고서(PE787.987)는 6월 30일, 위원회 수정안은 7월 28일에 올라왔습니다. 시장내부·소비자보호 위원회(IMCO)는 10월 15일 의견 보고관을 지명했습니다.",
    "EU 이사회에서는 의약품·의료기기 작업반이 2026년 4~6월에 집행위의 분야별 설명을 받고 회원국 의견서를 모았습니다. 예를 들어 인증기관·분류·적합성평가를 다루는 묶음이 있습니다.",
    "유럽의회 절차 페이지의 예상 일정에는 1차 독회 본회의 예정일이 2026년 12월 14일로 표시되어 있습니다. 이는 예정일이며, 위원회 표결일은 아직 게재되지 않았습니다.",
   ],
   "check": "개정안은 입법 진행 중이며 내용과 일정은 바뀔 수 있습니다. 아직 시행된 규정이 아닙니다.",
  },
  "en": {
   "title": "EU MDR/IVDR simplification proposal: Parliament committee draft report and amendments",
   "sum": "The European Commission proposed the MDR/IVDR simplification on 16 December 2025. The Parliament's public health committee (SANT) published a draft report on 30 June 2026 and amendments on 28 July.",
   "points": [
    "The proposal (COM(2025)1023) amends the MDR and IVDR, together with the rules on EMA support for expert panels (Regulation (EU) 2022/123) and the Annex I list of the AI Act (Regulation (EU) 2024/1689). Its aim is to simplify the rules and reduce the burden.",
    "In Parliament, SANT is the responsible committee and Oliver Schenk (EPP) is rapporteur, appointed on 13 February 2026. The draft report (PE787.987) is dated 30 June and the committee amendments 28 July. The IMCO committee appointed its rapporteur for opinion on 15 October.",
    "In the Council, the Working Party on Pharmaceuticals and Medical Devices received Commission presentations and Member State comments in April to June 2026, in thematic clusters such as notified bodies, classification and conformity assessment.",
    "The forecast on Parliament's procedure page shows an indicative first-reading plenary date of 14 December 2026. This is an indicative date, and no committee vote date is listed.",
   ],
   "check": "The proposal is still going through the legislative process; content and timing may change. It is not yet in force.",
  },
  "src": [
   ("유럽집행위원회 개정안 COM(2025)1023 (PDF)", "European Commission proposal COM(2025)1023 (PDF)", "https://health.ec.europa.eu/document/download/25e7ea7c-cab3-40cf-86d9-d11f5e7744d8_en?filename=md_com_2025-1023_act_en.pdf"),
   ("유럽의회 입법 절차 파일 2025/0404(COD)", "European Parliament procedure file 2025/0404(COD)", "https://oeil.europarl.europa.eu/oeil/en/procedure-file?reference=2025%2F0404%28COD%29"),
   ("EU 이사회 작업반 문서 (2026-05-07)", "Council working party document (7 May 2026)", "https://data.consilium.europa.eu/doc/document/WK-6502-2026-INIT/en/pdf"),
  ],
 },
 {
  "slug": "uk-mhra-draft-regulations", "date": "2026-05-08", "region": "uk", "svc": "technical-documentation",
  "ko": {
   "title": "영국 MHRA, 의료기기 시판 전 요건 개정 규정(Medical Devices (Amendment) Regulations 2026) 초안 공개",
   "sum": "MHRA가 2026년 5월 8일 WTO 통보 포털에 영국(GB) 시장 진입 의료기기·체외진단기기의 시판 전 요건을 담은 개정 규정 초안을 게시했습니다.",
   "points": [
    "초안의 이름은 'draft Medical Devices (Amendment) Regulations 2026'입니다. MHRA는 5월 11일 공지로 이를 알렸습니다.",
    "MHRA의 이행 계획 문서는 이 시판 전 규정이 국제 신뢰(international reliance) 제도를 도입해, 비교 가능한 규제기관이 이미 승인한 기기가 더 빨리 시장에 접근하도록 한다고 설명합니다.",
    "MHRA는 앞서 호주·캐나다·미국 규제기관의 승인을 활용하는 신뢰 경로를 추진하겠다고 밝힌 바 있습니다.",
    "2026년 2월 16일에는 CE 마크 기기의 무기한 인정에 관한 의견수렴도 시작했습니다. 의제는 MDD 인증 기기의 경과 기간 연장, EU MDR·IVDR 인증 기기의 무기한 인정, 영국 분류가 더 높은 일부 기기를 위한 신뢰 경로 등입니다.",
   ],
   "check": "초안이며 확정된 규정이 아닙니다. 최종 내용은 MHRA 공지를 확인하세요.",
  },
  "en": {
   "title": "UK MHRA publishes draft Medical Devices (Amendment) Regulations 2026 on pre-market requirements",
   "sum": "On 8 May 2026 the MHRA published, on the WTO notification portal, draft regulations setting new pre-market requirements for medical devices and IVDs entering the Great Britain market.",
   "points": [
    "The draft is titled 'draft Medical Devices (Amendment) Regulations 2026'. The MHRA announced it in a notice dated 11 May.",
    "The MHRA's implementation document says these pre-market regulations will introduce an international reliance framework, allowing swifter access for devices already approved by comparable regulators.",
    "The MHRA has earlier said it intends reliance routes using approvals from regulators in Australia, Canada and the United States.",
    "On 16 February 2026 it also launched a consultation on indefinite recognition of CE-marked devices, covering an extension of MDD transitional arrangements, indefinite recognition of EU MDR/IVDR-certified devices, and a reliance route for some devices that fall into a higher class under GB rules.",
   ],
   "check": "This is a draft, not final law. Check MHRA announcements for the final content.",
  },
  "src": [
   ("MHRA 공지 (2026-05-11)", "MHRA notice (11 May 2026)", "https://www.gov.uk/government/news/mhra-invites-views-on-proposed-changes-to-medical-device-regulation"),
   ("GOV.UK: 향후 의료기기 규제의 이행", "GOV.UK: implementation of the future regulations", "https://www.gov.uk/government/publications/implementation-of-the-future-regulation-of-medical-devices/implementation-of-the-future-regulations"),
   ("MHRA: CE 마크 의료기기 무기한 인정 의견수렴 (2026-02-16)", "MHRA: consultation on indefinite recognition of CE-marked devices", "https://www.gov.uk/government/news/mhra-launches-a-consultation-on-indefinite-recognition-of-ce-marked-medical-devices"),
   ("MHRA: 국제 신뢰 경로 추진 계획 발표", "MHRA: proposals on international reliance routes", "https://www.gov.uk/government/news/mhra-announces-proposals-to-improve-access-to-worlds-best-medical-devices-for-patients-and-to-boost-economic-growth-in-britains-med-tech-sector"),
  ],
 },
 {
  "slug": "kr-digital-classification", "date": "2026-03-20", "region": "kr", "svc": "digital-medical-products",
  "ko": {
   "title": "식약처, 디지털의료기기 분류 및 등급 지정 가이드라인 개정",
   "sum": "식약처가 2026년 3월 20일 보도참고자료로 「디지털의료기기 분류 및 등급 지정 가이드라인」 개정을 알렸습니다.",
   "points": [
    "보도참고자료는 디지털의료제품지원총괄과 명의로 3월 20일 게시됐습니다.",
    "앞서 2026년 1월 23일에는 「디지털의료제품 분류 및 등급 지정 등에 관한 규정」 일부개정고시(제2026-4호)로 디지털의료·건강지원기기의 범위가 지정됐습니다.",
    "이전 가이드라인은 디지털의료제품법 시행(2025년 1월 24일)에 맞춰 2025년 11월 6일에 안내서(안내서-1455-01)로 게시된 바 있습니다.",
   ],
   "check": "이번 개정에서 달라진 분류 기준은 보도참고자료와 가이드라인 원문에서 확인하세요.",
  },
  "en": {
   "title": "MFDS revises the guideline on classification and grading of digital medical devices",
   "sum": "On 20 March 2026 MFDS announced a revision of its guideline on classification and grading of digital medical devices in a press reference document.",
   "points": [
    "The press reference document was posted on 20 March under the Digital Medical Products Support Division.",
    "Earlier, on 23 January 2026, an amendment to the rule on classification and grading of digital medical products (Notice No. 2026-4) specified the scope of digital medical and health support devices.",
    "The previous guideline was posted as 안내서-1455-01 on 6 November 2025, following the Digital Medical Products Act taking effect on 24 January 2025.",
   ],
   "check": "Check the press document and the guideline itself for the revised classification criteria.",
  },
  "src": [
   ("식약처 보도참고자료 (2026-03-20)", "MFDS press reference (2026-03-20)", "https://mfds.go.kr/brd/m_99/view.do?seq=49774"),
   ("정책브리핑: 보도참고 (2026-03-20)", "Korea Policy Briefing: press reference", "https://www.korea.kr/briefing/pressReleaseView.do?newsId=156749940&call_from=rsslink"),
   ("식약처 고시 제2026-4호 (디지털의료제품 분류 및 등급 지정 등에 관한 규정)", "MFDS Notice No. 2026-4", "https://mfds.go.kr/brd/m_207/view.do?seq=15133"),
   ("식약처 민원인 안내서: 디지털의료기기 분류 및 등급 지정 등에 관한 가이드라인", "MFDS guideline page: classification and grading", "https://mfds.go.kr/brd/m_1060/view.do?seq=15749"),
  ],
 },
 {
  "slug": "cn-nmpa-standards-2026", "date": "2026-09-14", "region": "cn", "svc": "risk-management",
  "ko": {
   "title": "중국 NMPA, 2026년 의료기기 업계표준 잇따라 발표(3월 26종, 8월 46종, 9월 AI 데이터셋 표준)",
   "sum": "NMPA의 의료기기 업계표준 공고 목록에 2026년 3월 17일 26종, 8월 14일 46종, 9월 14일 1종의 발표 공고가 올라 있습니다.",
   "points": [
    "2026년 제24호 공고(3월 17일): 「골접합 임플란트 금속 접골판」 등 의료기기 업계표준 26종 발표. 같은 날 제26호 공고로 2종을 폐지했습니다.",
    "2026년 제76호 공고(8월 14일): 「치과학 광중합기」 등 46종 발표.",
    "2026년 제79호 공고(9월 14일): YY/T 2029—2026 「뇌-컴퓨터 인터페이스 의료기기 인공지능 알고리즘용 뇌전도 데이터셋의 품질 요구사항 및 평가 방법」 발표.",
    "중국 국가표준정보공공서비스플랫폼에는 YY/T 1406-2026 「의료기기 소프트웨어: GB/T 42062의 의료기기 소프트웨어 적용 지침」이 2026년 3월 9일 발행, 2027년 3월 1일 시행으로 등재되어 있습니다. GB/T 42062는 ISO 14971:2019와 동등한 국가표준입니다.",
   ],
   "check": "각 표준의 시행일과 적용 범위는 공고 본문과 표준 원문에서 확인하세요. YY/T 1406-2026이 위 26종 공고에 포함되는지는 확인하지 못했습니다.",
  },
  "en": {
   "title": "China NMPA publishes medical device industry standards through 2026 (26 in March, 46 in August, an AI dataset standard in September)",
   "sum": "NMPA's medical device industry standard announcements list 26 standards on 17 March 2026, 46 on 14 August and one on 14 September.",
   "points": [
    "Announcement No. 24 of 2026 (17 March): 26 medical device industry standards, including 'Osteosynthesis implants: metal bone plates'. Announcement No. 26 of the same day withdrew two standards.",
    "Announcement No. 76 of 2026 (14 August): 46 standards, including 'Dentistry: light-curing units'.",
    "Announcement No. 79 of 2026 (14 September): YY/T 2029-2026, quality requirements and evaluation methods for EEG datasets used in AI algorithms for brain-computer interface medical devices.",
    "China's national standards information platform lists YY/T 1406-2026, 'Medical device software: guidance on applying GB/T 42062 to medical device software', published 9 March 2026 and effective 1 March 2027. GB/T 42062 is the national standard equivalent to ISO 14971:2019.",
   ],
   "check": "Check the announcements and the standards themselves for effective dates and scope. We could not confirm whether YY/T 1406-2026 is among the 26 standards in the March announcement.",
  },
  "src": [
   ("NMPA 의료기기 업계표준 공고 목록", "NMPA: medical device industry standard announcements", "https://www.nmpa.gov.cn/directory/web/nmpa/xxgk/ggtg/ylqxggtg/ylqxhybzhgg/index.html"),
   ("전국표준정보공공서비스플랫폼: YY/T 1406-2026 검색 결과", "National Public Service Platform for Standards Information: YY/T 1406-2026", "https://std.samr.gov.cn/search/stdPage?q=42062&tid="),
  ],
 },
 {
  "slug": "us-qmsr-cybersecurity", "date": "2026-02-03", "region": "us", "svc": "qms",
  "ko": {
   "title": "FDA QMSR 시행(2월 2일), 사이버보안 지침을 QMSR 기준으로 재발행(2월 3일)",
   "sum": "미국 FDA의 품질경영시스템규정(QMSR)이 2026년 2월 2일 시행됐고, 사이버보안 지침이 QMSR 용어와 기준으로 다시 발행됐습니다.",
   "points": [
    "21 CFR Part 820이 QMSR로 바뀌어 2월 2일 시행됐습니다. 기존 Part 820 요구사항 대부분을 고치고 ISO 13485:2016을 인용해 포함합니다.",
    "FDA는 2월 2일부터 품질시스템 점검 기법(QSIT) 대신 개정된 점검 프로그램 7382.850을 사용하며, 7382.845와 7383.001은 더 이상 쓰지 않습니다.",
    "사이버보안 지침 「Cybersecurity in Medical Devices: Quality Management System Considerations and Content of Premarket Submissions」가 2026년 2월 3일자로 발행되어 2025년 6월 27일판을 대체합니다.",
    "이 지침은 소프트웨어(펌웨어 포함)나 프로그램 가능한 로직을 포함하는 등 사이버보안 고려가 필요한 기기에 적용되며, 네트워크에 연결되는 기기에 한정되지 않습니다.",
   ],
  },
  "en": {
   "title": "FDA QMSR takes effect 2 February; cybersecurity guidance reissued on 3 February",
   "sum": "The FDA Quality Management System Regulation (QMSR) took effect on 2 February 2026, and the cybersecurity guidance was reissued with QMSR terminology and basis.",
   "points": [
    "21 CFR Part 820 became the QMSR on 2 February. It amends most of the previous Part 820 requirements and incorporates ISO 13485:2016 by reference.",
    "From 2 February the FDA stopped using the Quality System Inspection Technique (QSIT) and uses the updated Compliance Program 7382.850. It no longer uses 7382.845 or 7383.001.",
    "The guidance 'Cybersecurity in Medical Devices: Quality Management System Considerations and Content of Premarket Submissions' is dated 3 February 2026 and supersedes the 27 June 2025 version.",
    "It applies to devices with cybersecurity considerations, including devices with software (including firmware) or programmable logic. It is not limited to network-connected devices.",
   ],
  },
  "src": [
   ("FDA: QMSR 자주 묻는 질문", "FDA: QMSR frequently asked questions", "https://www.fda.gov/medical-devices/quality-management-system-regulation-qmsr/quality-management-system-regulation-frequently-asked-questions"),
   ("FDA: 의료기기 제조업체 점검 프로그램 7382.850", "FDA: Compliance Program 7382.850", "https://www.fda.gov/media/80195/download"),
   ("FDA: 사이버보안 지침 (2026-02-03)", "FDA: cybersecurity guidance (3 Feb 2026)", "https://www.fda.gov/media/119933/download"),
  ],
 },
 {
  "slug": "us-cds-general-wellness", "date": "2026-01-29", "region": "us", "svc": "technical-documentation",
  "ko": {
   "title": "FDA, 임상의사결정지원(CDS) 소프트웨어와 일반 웰니스 최종 지침 개정",
   "sum": "FDA가 2026년 1월 6일 일반 웰니스 지침과 CDS 소프트웨어 지침의 최종판을 발행했고, CDS 지침은 1월 29일 다시 발행했습니다.",
   "points": [
    "「General Wellness: Policy for Low Risk Devices」가 2026년 1월 6일자로 발행되어 2019년 9월 27일판을 대체합니다. 웨어러블 등의 비침습 센싱 기술이 일반 웰니스 제품으로 남을 수 있는 경우를 명확히 했다고 FDA가 설명했습니다.",
    "「Clinical Decision Support Software」는 2026년 1월 29일자 문서가 1월 6일판을 대체합니다.",
    "CDS 지침은 의료전문가용 임상의사결정지원 소프트웨어에 대한 FDA 감독 범위를 설명하고, 법 제520조(o)(1)(E)에 따라 의료기기에서 제외되는 기능(비기기 CDS)의 기준을 다룹니다. 기기에 해당하는 소프트웨어 기능에는 기존 디지털 헬스 정책이 계속 적용됩니다.",
    "FDA는 2026년 3월 11일 CDS 최종 지침에 관한 타운홀을 열었습니다.",
   ],
  },
  "en": {
   "title": "FDA updates final guidance on clinical decision support software and general wellness",
   "sum": "The FDA issued final general wellness and clinical decision support (CDS) software guidance on 6 January 2026, and reissued the CDS guidance on 29 January.",
   "points": [
    "'General Wellness: Policy for Low Risk Devices' is dated 6 January 2026 and supersedes the 27 September 2019 version. The FDA explained that it clarifies how non-invasive sensing technology, common in wearables, can remain a general wellness product.",
    "'Clinical Decision Support Software' dated 29 January 2026 supersedes the 6 January version.",
    "The CDS guidance describes the scope of FDA oversight of CDS software for health care professionals and the criteria for functions excluded from the device definition under section 520(o)(1)(E) (non-device CDS). Existing digital health policies continue to apply to software functions that are devices.",
    "The FDA held a town hall on the final CDS guidance on 11 March 2026.",
   ],
  },
  "src": [
   ("FDA: Clinical Decision Support Software 지침", "FDA: Clinical Decision Support Software guidance", "https://www.fda.gov/media/109618/download"),
   ("FDA: General Wellness 지침", "FDA: General Wellness guidance", "https://www.fda.gov/media/90652/download"),
   ("FDA: CDS 최종 지침 타운홀 (2026-03-11)", "FDA: CDS final guidance town hall (11 Mar 2026)", "https://www.fda.gov/medical-devices/medical-devices-news-and-events/town-hall-clinical-decision-support-software-final-guidance-03112026"),
  ],
 },
 {
  "slug": "kr-approval-rules-cybersecurity", "date": "2026-01-26", "region": "kr", "svc": "cybersecurity",
  "ko": {
   "title": "식약처, 의료기기·체외진단의료기기 허가 규정 개정: 사이버보안 심사자료 제출 근거 정리",
   "sum": "식약처가 2026년 1월 26일 「의료기기 허가·신고·심사 등에 관한 규정」(고시 제2026-6호)과 「체외진단의료기기 허가·신고·심사 등에 관한 규정」(제2026-7호)을 개정했습니다.",
   "points": [
    "체외진단의료기기 규정(제2026-7호)은 사이버보안의 정의를 신설하고, 허가 신청서의 '모양 및 구조'와 '사용 시 주의사항'에 사이버보안 내용을 적도록 했습니다. 기술문서 등 심사 시 첨부자료 요건에는 사이버보안 적용 사항을 추가했습니다.",
    "같은 규정(제2026-7호)은 신의료기술평가 유예를 받으려는 경우 임상적성능평가 자료로 허가·인증을 신청할 수 있게 하고, 신개발체외진단의료기기의 허가·심사 지원 근거도 담았습니다.",
    "의료기기 규정은 2025년 행정예고(공고 제2025-195호)에서 사이버보안 정의 신설, 신개발의료기기를 신속심사 대상에 추가, 시판 후 조사기간 중 동등성 검토를 통한 임상시험자료 면제 제한을 예고했습니다.",
   ],
   "check": "의료기기 규정(제2026-6호)의 최종 개정 내용은 고시 원문에서 확인하세요. 위의 의료기기 규정 내용은 행정예고안 기준입니다.",
  },
  "en": {
   "title": "MFDS amends approval rules for medical devices and IVDs, clarifying cybersecurity submission data",
   "sum": "On 26 January 2026 MFDS amended the Regulation on Approval, Notification and Review of Medical Devices (Notice No. 2026-6) and the corresponding IVD regulation (No. 2026-7).",
   "points": [
    "The IVD regulation (No. 2026-7) adds a definition of cybersecurity and requires cybersecurity information in the 'shape and structure' and 'precautions for use' fields of the application. It adds cybersecurity to the requirements for attachments in technical documentation review.",
    "The same regulation allows applicants seeking a deferral of new health technology assessment to apply for approval or certification with clinical performance evaluation data, and adds support for reviewing new IVDs.",
    "For the medical device regulation, the 2025 administrative notice (No. 2025-195) proposed adding a cybersecurity definition, adding new medical devices to the fast-track review targets, and limiting the clinical data exemption through equivalence review during the post-market survey period.",
   ],
   "check": "Check the notice itself for the final content of the medical device regulation (No. 2026-6). The medical device points above are based on the proposed text.",
  },
  "src": [
   ("식약처 고시 제2026-6호 (의료기기 허가·신고·심사 등에 관한 규정)", "MFDS Notice No. 2026-6 (medical devices)", "https://mfds.go.kr/brd/m_207/view.do?seq=15135"),
   ("식약처 고시 제2026-7호 (체외진단의료기기 허가·신고·심사 등에 관한 규정)", "MFDS Notice No. 2026-7 (IVDs)", "https://mfds.go.kr/brd/m_207/view.do?seq=15136"),
   ("식약처 행정예고 공고 제2025-195호", "MFDS administrative notice No. 2025-195", "https://www.mfds.go.kr/law/board/boardDetail.do?menuKey=33&brdId=data0009&seq=44096"),
  ],
 },
 {
  "slug": "iso-13485-confirmed", "date": "2025-10-31", "region": "intl", "svc": "qms",
  "ko": {
   "title": "ISO 13485:2016, 2025년 정기 검토에서 유지 확정",
   "sum": "ISO 사이트에서 ISO 13485:2016은 2025년 10월 31일 '국제표준 확정(confirmed)' 단계로 표시되며, 현재 판이 유효하다고 안내합니다.",
   "points": [
    "ISO 표준 페이지는 이 표준이 2025년에 검토·확정되었으며 현재 판이 유효하다고 적고 있습니다(수명주기 단계 90.93).",
    "ISO/TC 210은 2020년에 ISO 13485:2016의 다음 정기 검토를 2025년 1월 15일 이후에 시작하기로 정했습니다.",
    "별도로 ISO/CD TS 23485(ISO 13485:2016 적용 지침)가 개발 중입니다. 위원회 초안(30.99) 단계입니다.",
   ],
  },
  "en": {
   "title": "ISO 13485:2016 confirmed after its 2025 systematic review",
   "sum": "ISO's website shows ISO 13485:2016 at the 'International Standard confirmed' stage on 31 October 2025, and states that the current edition remains valid.",
   "points": [
    "The ISO standard page says the publication was reviewed and confirmed in 2025 and that this version remains current (life cycle stage 90.93).",
    "ISO/TC 210 agreed in 2020 that the next systematic review of ISO 13485:2016 would not open until 15 January 2025.",
    "Separately, ISO/CD TS 23485, guidance for applying ISO 13485:2016, is under development at committee draft stage (30.99).",
   ],
  },
  "src": [
   ("ISO: ISO 13485:2016 표준 페이지", "ISO: ISO 13485:2016 standard page", "https://www.iso.org/standard/59752.html"),
   ("ISO: ISO/CD TS 23485 (개발 중)", "ISO: ISO/CD TS 23485 (under development)", "https://www.iso.org/standard/90565.html"),
   ("ISO/TC 210: 진행 중인 프로젝트", "ISO/TC 210: ongoing projects", "https://committee.iso.org/sites/tc210/home/projects/ongoing/ongoing-1/content-left-area/iso-80369-series---small-bore-co/ongoing-projects-in-iso-tc-210.html"),
  ],
 },
]

from news_add import ADD
NEWS += ADD
NEWS.sort(key=lambda n: n["date"], reverse=True)
