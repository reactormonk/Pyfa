# Used by:
# Implants named like: Low grade Grail (6 of 6)
type = "passive"
runTime = "early"
def handler(fit, implant, context):
    fit.implants.filteredItemMultiply(lambda target: target.item.requiresSkill("Cybernetics"),
                                      "scanRadarStrengthModifier", implant.getModifiedItemAttr("implantSetLGImperialNavy"))