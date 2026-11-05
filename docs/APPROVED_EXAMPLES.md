# Style reference examples

These existing questions anchor the format established with the user. The SVT arrow-chain format was explicitly endorsed. The other examples illustrate its implementation across mechanisms, drugs and necessary corrections; they are not a claim that the user individually reviewed every medical statement. Full frozen records live in `docs/approved-examples.json`. Do not rewrite the reference records merely to make validation pass.

Compare new questions to these for brevity, one tested point and explanation structure. Sources are referenced by real page and asset keys in the JSON.

## cardio-svt-filling
Why can SVT cause hypotension?

**Answer:** Reduced diastolic filling

**Original note:** Re-entry → SVT → <strong>reduced diastolic filling</strong> → hypotension

**Explanation:** Fast rate → shorter diastole → less filling → lower stroke volume and cardiac output.

## cardio-pr-dhp
PR prolongation: why favor a DHP calcium channel blocker?

**Answer:** It mainly targets vascular smooth muscle

**Original note:** If someone has PR lengthening, DHP CCBs may be a good choice because it targets <strong>smooth muscle</strong>.

**Explanation:** DHPs → vascular smooth muscle. Verapamil/diltiazem → AV node → further PR prolongation.

## cardio-freewall-tamponade
Day 5 post-MI + JVD, hypotension, clear lungs, no new murmur → complication?

**Answer:** LV free-wall rupture → tamponade

**Original note:** Post-MI complication on day 5 with elevated jugular venous pressure, no murmurs, and clear lungs = <strong>cardiac tamponade secondary to free wall rupture</strong>.

**Explanation:** LV wall ruptures → blood enters pericardium → tamponade. No new murmur favors this over septal/papillary rupture.

## cardio-fibrates-lpl
Fibrates upregulate which enzyme?

**Answer:** Lipoprotein lipase

**Original note:** Fibrates: <strong>Increased LPL → breakdown TG in VLDL → clear TGs from blood.</strong>

**Explanation:** ↑ LPL → hydrolysis/clearance of TG in VLDL and chylomicrons.

## cardio-niacin-flush
Niacin → flushing. Which mediator?

**Answer:** Prostaglandins

**Original note:** Flushing: <strong>dilates vessels via prostaglandins</strong>.

**Explanation:** Niacin → prostaglandin-mediated cutaneous vasodilation → flushing.

## cardio-isoproterenol-receptor
Isoproterenol stimulates which receptors?

**Answer:** β1 and β2

**Original note:** Isoproterenol (beta blocker): second-line for severe bradycardia refractory to adenosine. <strong>Correction: β1/β2 agonist.</strong>

**Explanation:** Isoproterenol is a β agonist → ↑ HR and ↓ SVR. Adenosine treats certain tachycardias; atropine is the initial drug for symptomatic bradycardia.

## cardio-tr-systemic-congestion
TR → ascites and liver congestion. Why?

**Answer:** Backflow raises right atrial/systemic venous pressure

**Original note:** Tricuspid regurg ... shows up in the <strong>systemic circulation (fluid overload, ascites, liver issues)</strong>.

**Explanation:** RV-to-RA systolic backflow → ↑ systemic venous pressure → hepatic congestion/ascites.

## cardio-statin-enzyme
Statins inhibit which enzyme?

**Answer:** HMG-CoA reductase

**Original note:** Statins: <strong>MOA: HMG-CoA reductase inhibitors.</strong>

**Explanation:** Inhibit rate-limiting hepatic cholesterol synthesis → ↓ intracellular cholesterol → ↑ LDL receptors.
