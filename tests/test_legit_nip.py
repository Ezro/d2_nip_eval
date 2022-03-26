import json
import os
import pytest
from d2_nip_to_eval import lexer
from mock_hovered_items import MOCK_HOVERED_ITEMS


@pytest.mark.parametrize("nip_file, expected_file", [
    ('Barb_helms.nip', 'Barb_helms.json'),
    ('Boots_Gloves.nip', 'Boots_Gloves.json'),
    ('charms.nip', 'charms.json'),
    ('Circlets.nip', 'Circlets.json'),
    ('claws.nip', 'claws.json'),
    ('crafted.nip', 'crafted.json'),
    ('crafts.nip', 'crafts.json'),
    ('Jewels_rings_ammys_start.nip', 'Jewels_rings_ammys_start.json'),
    ('Jewels_rings_ammys.nip', 'Jewels_rings_ammys.json'),
    ('LLD.nip', 'LLD.json'),
    ('misc.nip', 'misc.json'),
    ('Random_rares.nip', 'Random_rares.json'),
    ('Rares.nip', 'Rares.json'),
    ('Shop_magic.nip', 'Shop_magic.json'),
    ('Socketable.nip', 'Socketable.json'),
    ('Unid_start_2.nip', 'Unid_start_2.json'),
    ('Unid_start_3.nip', 'Unid_start_3.json'),
    ('Unid.nip', 'Unid.json'),
    ('Uniques.nip', 'Uniques.json'),
    ('Whites_start.nip', 'Whites_start.json'),
    ('Whites.nip', 'Whites.json'),
])
def test_legit_nip_transpile(nip_file, expected_file):
    nip_file_path = os.path.join(
        os.path.dirname(__file__),
        'nip',
        'legit',
        nip_file)
    nip_file_lines = open(nip_file_path).readlines()
    expected_items_path = os.path.join(
        os.path.dirname(__file__),
        'nip',
        'legit',
        expected_file)
    eval_expressions = lexer.transpile_nip_expressions(nip_file_lines)
    expected_file_files = json.loads(open(expected_items_path).read())
    assert eval_expressions == expected_file_files


@pytest.mark.parametrize("nip_file", [
    ('misc.nip'),
])
def test_legit_eval_match(nip_file):
    nip_file_path = os.path.join(
        os.path.dirname(__file__),
        'nip',
        'legit',
        nip_file)
    nip_file_lines = open(nip_file_path).readlines()
    eval_expressions = lexer.transpile_nip_expressions(nip_file_lines)
    test_data_map = {
        'Zod': ['misc.nip'],
        '50_WarTraveler': ['Uniques.nip']
    }
    for mock_item_name in MOCK_HOVERED_ITEMS:
        should_keep_item = mock_item_name in test_data_map and nip_file in test_data_map[mock_item_name]
        item_data = MOCK_HOVERED_ITEMS[mock_item_name]
        keep_item = lexer.keep_item(eval_expressions, item_data)
        assert should_keep_item == keep_item


# import glob
# import json
# nip_file_paths = glob.glob('tests/nip/legit/*.nip')
# for nip_file_path in nip_file_paths:
#     data = open(nip_file_path).readlines()
#     expressions = lexer.transpile_nip_expressions(data)
#     json_file_path = nip_file_path.replace('.nip', '.json')
#     json_file = open(json_file_path, 'w')
#     json_file.write(json.dumps(expressions))
#     json_file.close()

# test_legit_eval_match('misc.nip')