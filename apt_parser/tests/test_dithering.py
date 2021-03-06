from parameterized import parameterized

from miri.apt_parser.utils import read_fake_xml, get_namespace
from miri.apt_parser.dithering import parse_dither

testdata = [
    ("""    <mmrs:MrsDitherSpecification>
        <mmrs:DitherType>4-Point</mmrs:DitherType>
        <mmrs:OptimizedFor>Channel 1</mmrs:OptimizedFor>
        <mmrs:Direction>Positive</mmrs:Direction>
    </mmrs:MrsDitherSpecification>""", 4),

    ("""    <mmrs:MrsDitherSpecification>
         <mmrs:DitherType>2-Point</mmrs:DitherType>
         <mmrs:OptimizedFor>Channel 1</mmrs:OptimizedFor>
         <mmrs:Direction>Negative</mmrs:Direction>
     </mmrs:MrsDitherSpecification>""", 2),

    ("""    <mi:DitherSpecification>
        <mi:DitherType>Sparse Cycling</mi:DitherType>
        <mi:StartingPoint>1</mi:StartingPoint>
        <mi:NumberOfPoints>100</mi:NumberOfPoints>
        <mi:Points>1,2,3-32</mi:Points>
        <mi:StartingSet>1</mi:StartingSet>
        <mi:NumberOfSets>1</mi:NumberOfSets>
        <mi:Direction>POSITIVE</mi:Direction>
        <mi:OptimizeFor>POINT SOURCE</mi:OptimizeFor>
        <mi:PatternSize>SMALL</mi:PatternSize>
    </mi:DitherSpecification>""", 32),  # APT 1028, obs_id 85

    ("""<mef:DitherSpec>
        <mef:DitherType>4-Point-Sets</mef:DitherType>
        <mef:StartingSet>1</mef:StartingSet>
        <mef:NumberOfSets>4</mef:NumberOfSets>
        <mef:Direction>POSITIVE</mef:Direction>
        <mef:OptimizeFor>POINT SOURCE</mef:OptimizeFor>
    </mef:DitherSpec>""", 16),  # APT 1027, obs_id 19
]


@parameterized(testdata)
def test_dithering(sample_xml, expected):
    """
    Test of dithering

    Sample from :
    APT STScI ID 1028 observation 85
    """

    namespace = get_namespace(sample_xml)

    tree = read_fake_xml(sample_xml)

    nb_dither = parse_dither(tree, namespace)

    assert nb_dither == expected, "Wrong number of dithering points, expected {}".format(expected)
