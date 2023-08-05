source "helpers.tcl"

# Open database, load lef and design

read_lef "data/Nangate45/NangateOpenCellLibrary.mod.lef"
read_def "data/gcd/gcd_nangate45_route_with_power_pins.def"

set lef_file [make_result_file gcd_abstract_lef_with_power.lef]

write_abstract_lef $lef_file

diff_file $lef_file "gcd_abstract_lef_with_power.lefok"