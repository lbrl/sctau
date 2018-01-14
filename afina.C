{
    TCanvas * c1 = new TCanvas("c1", "c1", 350*3, 350*2);
    c1->Divide(3, 2);
    /// pi+ total momentum
    c1->cd(1);
    events->SetLineWidth(2);
    events->SetLineColor(kRed);
    // events->Draw("(GenParticle.core.p4.px**2+GenParticle.core.p4.py**2+GenParticle.core.p4.pz**2)**.5", "GenParticle.core.pdgId==-211");
    events->Draw("(GenParticle.core.p4.px**2+GenParticle.core.p4.py**2+GenParticle.core.p4.pz**2)**.5",
            /// "GenParticle.core.pdgId==-211");
            "");
    events->SetLineColor(kBlue);
    /// events->Draw("(RecParticle.core.p4.px**2+RecParticle.core.p4.py**2+RecParticle.core.p4.pz**2)**.5", "RecParticle.core.pdgId==-211", "same");
    events->Draw("(RecParticle.core.p4.px**2+RecParticle.core.p4.py**2+RecParticle.core.p4.pz**2)**.5",
            "", "same");
    /// pi+ theta
    c1->cd(2);
    events->SetLineColor(kRed);
    // events->Draw("atan((GenParticle.core.p4.px**2+GenParticle.core.p4.py**2)**.5 / GenParticle.core.p4.pz)", "GenParticle.core.pdgId==-211");
    // events->Draw("asin((GenParticle.core.p4.px**2+GenParticle.core.p4.py**2)**.5 / (GenParticle.core.p4.px**2+GenParticle.core.p4.py**2+GenParticle.core.p4.pz**2)**.5)",
    events->Draw("acos(GenParticle.core.p4.pz / (GenParticle.core.p4.px**2+GenParticle.core.p4.py**2+GenParticle.core.p4.pz**2)**.5)",
            "GenParticle.core.pdgId==-211");
    events->SetLineColor(kBlue);
    // events->Draw("atan((RecParticle.core.p4.px**2+RecParticle.core.p4.py**2)**.5 / RecParticle.core.p4.pz)", "RecParticle.core.pdgId==-211", "same");
    // events->Draw("asin((RecParticle.core.p4.px**2+RecParticle.core.p4.py**2)**.5 / (RecParticle.core.p4.px**2+RecParticle.core.p4.py**2+RecParticle.core.p4.pz**2)**.5)",
    events->Draw("acos(RecParticle.core.p4.pz / (RecParticle.core.p4.px**2+RecParticle.core.p4.py**2+RecParticle.core.p4.pz**2)**.5)",
            "RecParticle.core.pdgId==-211", "same");
    /// pi+ momentum difference
    c1->cd(3);
    events->Draw("((RecParticle.core.p4.px**2+RecParticle.core.p4.py**2+RecParticle.core.p4.pz**2)**.5-(GenParticle.core.p4.px**2+GenParticle.core.p4.py**2+GenParticle.core.p4.pz**2)**.5)/(GenParticle.core.p4.px**2+GenParticle.core.p4.py**2+GenParticle.core.p4.pz**2)**.5 : (GenParticle.core.p4.px**2+GenParticle.core.p4.py**2+GenParticle.core.p4.pz**2)**.5",
            "RecParticle.core.pdgId==-211", "colz");
    c1->cd(4);
    events->Draw("((RecParticle.core.p4.px**2+RecParticle.core.p4.py**2+RecParticle.core.p4.pz**2)**.5-(GenParticle.core.p4.px**2+GenParticle.core.p4.py**2+GenParticle.core.p4.pz**2)**.5)/(GenParticle.core.p4.px**2+GenParticle.core.p4.py**2+GenParticle.core.p4.pz**2)**.5",
            "RecParticle.core.pdgId==-211", "colz");
    /// Photon theta
    c1->cd(5);
    events->SetLineColor(kRed);
    // events->Draw("atan((RecParticle.core.p4.px**2+RecParticle.core.p4.py**2)**.5 / RecParticle.core.p4.pz)", "RecParticle.core.pdgId==22", "");
    events->Draw("acos(RecParticle.core.p4.pz / (RecParticle.core.p4.px**2+RecParticle.core.p4.py**2+RecParticle.core.p4.pz**2)**.5)",
            "RecParticle.core.pdgId==22");
    c1->cd();
    c1->Update();
}
